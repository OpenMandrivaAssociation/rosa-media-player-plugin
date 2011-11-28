#This is a spec file for Mandriva Media Player Plugin

Summary:	ROSA Media Player Plugin
Name:		rosa-media-player-plugin
Version:	0.95
Release:	139
License:	GPL v.3
Group:		Video
Source:		%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel	>= 4.2.0
BuildRequires:	qt4-linguist	>= 4.2.0
Requires:	mplayer		>= 1.0-1.rc1
BuildRoot:	/tmp/rosamp-plugin

%undefine __find_requires

%description
ROSA Media Player Plugin

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
%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-smp.so
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-qt.so
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-wmp.so
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-dvx.so
%{_libdir}/mozilla/plugins/librosa-media-player-plugin-rm.so
%{_libdir}/librosampcore.so
%{_libdir}/librosampcore.so.1
%{_libdir}/librosampcore.so.1.0
%{_libdir}/librosampcore.so.1.0.0
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ar_SY.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_bg.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ca.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_cs.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_de.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_el_GR.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_en_US.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_es.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_et.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_eu.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_fi.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_fr.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_gl.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_hu.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_it.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ja.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ka.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ko.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ku.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_lt.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_mk.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_nl.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_pl.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_pt_BR.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_pt.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ro_RO.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_ru_RU.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_sk.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_sl_SI.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_sr.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_sv.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_tr.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_uk_UA.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_vi_VN.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_zh_CN.qm
%{_libdir}/mozilla/plugins/translations/rosamp_plugin_zh_TW.qm
