Summary:	XMMS Control plugin
Summary(pl):	Wtyczka do kontroli XMMS-a
Name:		xfce4-xmms-plugin
Version:	0.3.1
Release:	1
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	0dac8795b192383c13b1d5cd072b754a
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	automake
BuildRequires:	pango >= 1:1.8.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 3.99.2
BuildRequires:	xmms
BuildRequires:	xmms-devel
Requires:	pango >= 1:1.8.0
Requires:	xfce4-panel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which provide you control on XMMS from xfce4-panel.

%description -l pl
Wtyczka która umo¿liwia kontrolê nad XMMS-em z pozycji panelu Xfce.

%prep
%setup -q

%build
#cp -f /usr/share/automake/config.sub .
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
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/xmms-plugin
