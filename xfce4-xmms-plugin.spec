Summary:	XMMS, BMP or Audacious player control plugin
Summary(pl.UTF-8):	Wtyczka do kontroli odtwarzacza XMMS, BMP lub Audacious
Name:		xfce4-xmms-plugin
Version:	0.5.1
Release:	2
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-xmms-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	e2e48ba8f2de32e4fd7ab09083458e3f
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which provides you control on XMMS, BMP or Audacious media
player from Xfce panel.

%description -l pl.UTF-8
Wtyczka, która umożliwia kontrolę nad odtwarzaczem multimedialnym
XMMS, BMP lub Audacious z pozycji panelu Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-xmms-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-xmms-plugin.desktop
%{_datadir}/xfce4/xfce4-xmms-plugin
