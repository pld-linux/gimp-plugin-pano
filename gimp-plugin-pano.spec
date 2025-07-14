Summary:	Panotools GIMP Plug-In
Summary(pl.UTF-8):	Wtyczka Panotools dla GIMP-a
Name:		gimp-plugin-pano
Version:	0.1.0
%define	snap	20050403
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Applications/Graphics
# not yet on http://dl.sourceforge.net/panotools/
# cvs :pserver:anonymous@cvs.sourceforge.net:/cvsroot/panotools gimp-plugin-ng
Source0:	panotools-gimp-plugin-ng-%{snap}.tar.bz2
# Source0-md5:	bb4f34f17008d032c3f6211aff0a6996
Patch0:		panotools-gimp-plugin-ng-DESTDIR.patch
Patch1:		panotools-gimp-plugin-ng-pl.po-update.patch
URL:		http://panotools.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl >= 1.67
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 1:2.0
BuildRequires:	intltool >= 0.17
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	gimp >= 1:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package implements Panotools for GIMP 2.0 and later..

%description -l pl.UTF-8
Ten pakiet jest implementacją Panotools dla GIMP-a 2.0 i późniejszych.

%prep
%setup -q -n gimp-plugin-ng
%patch -P0 -p1
%patch -P1 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang PanoPlugin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f PanoPlugin.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %(gimptool --gimpplugindir)/plug-ins/PanoPlugin
%dir %{_datadir}/PanoPlugin
%dir %{_datadir}/PanoPlugin/help
%{_datadir}/PanoPlugin/help/en
# de,fr,pl help not translated
