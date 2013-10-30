%define debug_package %{nil}
Summary:	ROSA Media Player Plugin
Name:		rosa-media-player-plugin
Version:        1.0
Release:	3
URL:		https://abf.rosalinux.ru/import/rosa-media-player-plugin
License:        GPL 3+
Group:		Video
Source:		%{name}-%{version}.tar.gz
Source100:	rosa-media-player-plugin.rpmlintrc
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
Requires:	mplayer
Packager:	Denis Koryavov <denis.koryavov@rosalab.ru>

%if %{_use_internal_dependency_generator}
%define __noautoreq 'devel\\((.*)\\)'
%else
%define _requires_exceptions devel(
%endif

%description
ROSA Media Player Plugin is designed to use with internet browsers 
like Firefox and Chrome/Chromium.

%prep
%setup -c

%build
cd rosa-media-player
qmake rosampcore.pro
make
cd ..

cd rosamp-plugin
qmake rosamp-plugin-smp.pro
make
qmake rosamp-plugin-qt.pro
make
qmake rosamp-plugin-wmp.pro
make
qmake rosamp-plugin-dvx.pro
make
qmake rosamp-plugin-rm.pro
make
lrelease rosamp-plugin-qt.pro
cd ..

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/translations/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/
cp -f rosamp-plugin/build/librosa-media-player-plugin-smp.so $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-dvx.so $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-qt.so $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-rm.so $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
cp -f rosamp-plugin/build/librosa-media-player-plugin-wmp.so $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/
cp -f rosa-media-player/build/librosampcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/

cp -f rosamp-plugin/translations/*.qm $RPM_BUILD_ROOT/%{_libdir}/mozilla/plugins/translations/

cd rosa-media-player/build/
ln -s librosampcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/librosampcore.so.1.0
ln -s librosampcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/librosampcore.so.1
ln -s librosampcore.so.1.0.0 $RPM_BUILD_ROOT/%{_libdir}/librosampcore.so


%files
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-*
%{_libdir}/librosampcore*
%{_libdir}/mozilla/plugins/translations/rosamp_plugin*
