Summary:	XMMS Control plugin
Summary(pl):	Wtyczka do kontroli XMMS-a
Name:		xfce4-xmms-plugin
Version:	0.4.2
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-xmms-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	d621fa744d534c17590848dc34884824
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-xmms-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.3.90.2
BuildRequires:	xfce4-panel-devel >= 4.3.90.2
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which provide you control on XMMS from xfce4-panel.

%description -l pl
Wtyczka która umo¿liwia kontrolê nad XMMS-em z pozycji panelu Xfce.

%prep
%setup -q

%build
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
