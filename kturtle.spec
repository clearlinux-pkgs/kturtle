#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kturtle
Version  : 22.12.2
Release  : 51
URL      : https://download.kde.org/stable/release-service/22.12.2/src/kturtle-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/kturtle-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/kturtle-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kturtle-bin = %{version}-%{release}
Requires: kturtle-data = %{version}-%{release}
Requires: kturtle-license = %{version}-%{release}
Requires: kturtle-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<img src="https://invent.kde.org/kde/kturtle/raw/master/src/turtle.svg" align="right"
title="Kturtle logo" width="64" height="64">

%package bin
Summary: bin components for the kturtle package.
Group: Binaries
Requires: kturtle-data = %{version}-%{release}
Requires: kturtle-license = %{version}-%{release}

%description bin
bin components for the kturtle package.


%package data
Summary: data components for the kturtle package.
Group: Data

%description data
data components for the kturtle package.


%package doc
Summary: doc components for the kturtle package.
Group: Documentation

%description doc
doc components for the kturtle package.


%package license
Summary: license components for the kturtle package.
Group: Default

%description license
license components for the kturtle package.


%package locales
Summary: locales components for the kturtle package.
Group: Default

%description locales
locales components for the kturtle package.


%prep
%setup -q -n kturtle-22.12.2
cd %{_builddir}/kturtle-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676858211
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676858211
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kturtle
cp %{_builddir}/kturtle-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kturtle/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
cp %{_builddir}/kturtle-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kturtle/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kturtle-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kturtle/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
pushd clr-build
%make_install
popd
%find_lang kturtle

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kturtle

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kturtle.desktop
/usr/share/icons/hicolor/128x128/apps/kturtle.png
/usr/share/icons/hicolor/16x16/apps/kturtle.png
/usr/share/icons/hicolor/22x22/apps/kturtle.png
/usr/share/icons/hicolor/32x32/apps/kturtle.png
/usr/share/icons/hicolor/48x48/apps/kturtle.png
/usr/share/icons/hicolor/64x64/apps/kturtle.png
/usr/share/kxmlgui5/kturtle/kturtleui.rc
/usr/share/metainfo/org.kde.kturtle.appdata.xml
/usr/share/xdg/kturtle.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kturtle/getting-started.docbook
/usr/share/doc/HTML/ca/kturtle/glossary.docbook
/usr/share/doc/HTML/ca/kturtle/index.cache.bz2
/usr/share/doc/HTML/ca/kturtle/index.docbook
/usr/share/doc/HTML/ca/kturtle/programming-reference.docbook
/usr/share/doc/HTML/ca/kturtle/translator-guide.docbook
/usr/share/doc/HTML/ca/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/de/kturtle/getting-started.docbook
/usr/share/doc/HTML/de/kturtle/glossary.docbook
/usr/share/doc/HTML/de/kturtle/index.cache.bz2
/usr/share/doc/HTML/de/kturtle/index.docbook
/usr/share/doc/HTML/de/kturtle/mainwindow.png
/usr/share/doc/HTML/de/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/de/kturtle/programming-reference.docbook
/usr/share/doc/HTML/de/kturtle/translator-guide.docbook
/usr/share/doc/HTML/de/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/en/kturtle/getting-started.docbook
/usr/share/doc/HTML/en/kturtle/glossary.docbook
/usr/share/doc/HTML/en/kturtle/index.cache.bz2
/usr/share/doc/HTML/en/kturtle/index.docbook
/usr/share/doc/HTML/en/kturtle/mainwindow.png
/usr/share/doc/HTML/en/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/en/kturtle/media-playback-start.png
/usr/share/doc/HTML/en/kturtle/programming-reference.docbook
/usr/share/doc/HTML/en/kturtle/translator-guide.docbook
/usr/share/doc/HTML/en/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/es/kturtle/getting-started.docbook
/usr/share/doc/HTML/es/kturtle/glossary.docbook
/usr/share/doc/HTML/es/kturtle/index.cache.bz2
/usr/share/doc/HTML/es/kturtle/index.docbook
/usr/share/doc/HTML/es/kturtle/mainwindow.png
/usr/share/doc/HTML/es/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/es/kturtle/print.png
/usr/share/doc/HTML/es/kturtle/programming-reference.docbook
/usr/share/doc/HTML/es/kturtle/translator-guide.docbook
/usr/share/doc/HTML/es/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/es/kturtle/wrapping.png
/usr/share/doc/HTML/et/kturtle/getting-started.docbook
/usr/share/doc/HTML/et/kturtle/glossary.docbook
/usr/share/doc/HTML/et/kturtle/index.cache.bz2
/usr/share/doc/HTML/et/kturtle/index.docbook
/usr/share/doc/HTML/et/kturtle/programming-reference.docbook
/usr/share/doc/HTML/et/kturtle/translator-guide.docbook
/usr/share/doc/HTML/et/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/fr/kturtle/forward.png
/usr/share/doc/HTML/fr/kturtle/getting-started.docbook
/usr/share/doc/HTML/fr/kturtle/glossary.docbook
/usr/share/doc/HTML/fr/kturtle/index.cache.bz2
/usr/share/doc/HTML/fr/kturtle/index.docbook
/usr/share/doc/HTML/fr/kturtle/mainwindow.png
/usr/share/doc/HTML/fr/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/fr/kturtle/programming-reference.docbook
/usr/share/doc/HTML/fr/kturtle/translator-guide.docbook
/usr/share/doc/HTML/fr/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/gl/kturtle/getting-started.docbook
/usr/share/doc/HTML/gl/kturtle/glossary.docbook
/usr/share/doc/HTML/gl/kturtle/index.cache.bz2
/usr/share/doc/HTML/gl/kturtle/index.docbook
/usr/share/doc/HTML/gl/kturtle/programming-reference.docbook
/usr/share/doc/HTML/gl/kturtle/translator-guide.docbook
/usr/share/doc/HTML/gl/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/it/kturtle/getting-started.docbook
/usr/share/doc/HTML/it/kturtle/glossary.docbook
/usr/share/doc/HTML/it/kturtle/index.cache.bz2
/usr/share/doc/HTML/it/kturtle/index.docbook
/usr/share/doc/HTML/it/kturtle/programming-reference.docbook
/usr/share/doc/HTML/it/kturtle/translator-guide.docbook
/usr/share/doc/HTML/it/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/nl/kturtle/getting-started.docbook
/usr/share/doc/HTML/nl/kturtle/glossary.docbook
/usr/share/doc/HTML/nl/kturtle/index.cache.bz2
/usr/share/doc/HTML/nl/kturtle/index.docbook
/usr/share/doc/HTML/nl/kturtle/mainwindow.png
/usr/share/doc/HTML/nl/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/nl/kturtle/programming-reference.docbook
/usr/share/doc/HTML/nl/kturtle/translator-guide.docbook
/usr/share/doc/HTML/nl/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/nl/kturtle/wrapping.png
/usr/share/doc/HTML/pt/kturtle/getting-started.docbook
/usr/share/doc/HTML/pt/kturtle/glossary.docbook
/usr/share/doc/HTML/pt/kturtle/index.cache.bz2
/usr/share/doc/HTML/pt/kturtle/index.docbook
/usr/share/doc/HTML/pt/kturtle/programming-reference.docbook
/usr/share/doc/HTML/pt/kturtle/translator-guide.docbook
/usr/share/doc/HTML/pt/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/pt_BR/kturtle/getting-started.docbook
/usr/share/doc/HTML/pt_BR/kturtle/glossary.docbook
/usr/share/doc/HTML/pt_BR/kturtle/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kturtle/index.docbook
/usr/share/doc/HTML/pt_BR/kturtle/mainwindow.png
/usr/share/doc/HTML/pt_BR/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/pt_BR/kturtle/programming-reference.docbook
/usr/share/doc/HTML/pt_BR/kturtle/translator-guide.docbook
/usr/share/doc/HTML/pt_BR/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/ru/kturtle/getting-started.docbook
/usr/share/doc/HTML/ru/kturtle/glossary.docbook
/usr/share/doc/HTML/ru/kturtle/index.cache.bz2
/usr/share/doc/HTML/ru/kturtle/index.docbook
/usr/share/doc/HTML/ru/kturtle/mainwindow.png
/usr/share/doc/HTML/ru/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/ru/kturtle/programming-reference.docbook
/usr/share/doc/HTML/ru/kturtle/translator-guide.docbook
/usr/share/doc/HTML/ru/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/sq/kturtle/getting-started.docbook
/usr/share/doc/HTML/sq/kturtle/glossary.docbook
/usr/share/doc/HTML/sq/kturtle/index.cache.bz2
/usr/share/doc/HTML/sq/kturtle/index.docbook
/usr/share/doc/HTML/sq/kturtle/mainwindow.png
/usr/share/doc/HTML/sq/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/sq/kturtle/programming-reference.docbook
/usr/share/doc/HTML/sq/kturtle/translator-guide.docbook
/usr/share/doc/HTML/sq/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/sv/kturtle/getting-started.docbook
/usr/share/doc/HTML/sv/kturtle/glossary.docbook
/usr/share/doc/HTML/sv/kturtle/index.cache.bz2
/usr/share/doc/HTML/sv/kturtle/index.docbook
/usr/share/doc/HTML/sv/kturtle/mainwindow.png
/usr/share/doc/HTML/sv/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/sv/kturtle/programming-reference.docbook
/usr/share/doc/HTML/sv/kturtle/translator-guide.docbook
/usr/share/doc/HTML/sv/kturtle/using-kturtle.docbook
/usr/share/doc/HTML/uk/kturtle/getting-started.docbook
/usr/share/doc/HTML/uk/kturtle/glossary.docbook
/usr/share/doc/HTML/uk/kturtle/index.cache.bz2
/usr/share/doc/HTML/uk/kturtle/index.docbook
/usr/share/doc/HTML/uk/kturtle/mainwindow.png
/usr/share/doc/HTML/uk/kturtle/mainwindow_flower_nrs.png
/usr/share/doc/HTML/uk/kturtle/programming-reference.docbook
/usr/share/doc/HTML/uk/kturtle/translator-guide.docbook
/usr/share/doc/HTML/uk/kturtle/using-kturtle.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kturtle/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kturtle/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kturtle/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kturtle.lang
%defattr(-,root,root,-)

