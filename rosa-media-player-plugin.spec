%define major 1
%define librosampcore %mklibname rosampcore %{major}
%define _disable_ld_no_undefined 1

Summary:	ROSA Media Player Plugin
Name:		rosa-media-player-plugin
Version:	1.6
Release:	5
License:	GPLv3+
Group:		Video
Url:		https://abf.rosalinux.ru/import/rosa-media-player-plugin
Source0:	%{name}-%{version}.tar.gz
#Patch0:		rosa-media-player-plugin-1.6-undefined.patch
BuildRequires:	qt4-linguist
BuildRequires:	qt4-devel
Requires:	mplayer

%description
ROSA Media Player Plugin is designed to use with internet browsers like Firefox
and Chrome/Chromium.

%files
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-*
%{_datadir}/rosa-media-player-plugin/translations/rosamp_plugin*

#----------------------------------------------------------------------------

%package -n %{librosampcore}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 1.6-5

%description -n %{librosampcore}
Shared library for %{name}.

%files -n %{librosampcore}
%{_libdir}/librosampcore.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q -c
#patch0 -p1

%build
mkdir build
cd build
%qmake_qt4 ../rosa-media-player-plugin.pro
%make
lrelease ../rosa-media-player-plugin.pro

%install
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/
mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/translations/
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_datadir}/rosa-media-player-plugin/translations/

echo $PWD
cd build
cp -f rosamp-plugin/build/librosa-media-player-plugin-smp.so %{buildroot}%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-dvx.so %{buildroot}%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-qt.so %{buildroot}%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-rm.so %{buildroot}%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-wmp.so %{buildroot}%{_libdir}/mozilla/plugins/
cp -f romp/rosa-media-player/build/librosampcore.so.1.0.0 %{buildroot}%{_libdir}/

cp -f ../translations/*.qm %{buildroot}%{_datadir}/rosa-media-player-plugin/translations/
cd romp/rosa-media-player/build/
ln -s librosampcore.so.1.0.0 %{buildroot}%{_libdir}/librosampcore.so.1.0
ln -s librosampcore.so.1.0.0 %{buildroot}%{_libdir}/librosampcore.so.1
