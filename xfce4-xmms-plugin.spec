Summary:	xfce4-xmms-plugin is an XMMS Control plugin
Summary(pl):	xfce4-xmms-plugin to wtyczka do kontroli XMMS-a
Name:		xfce4-xmms-plugin
Version:	0.1.1
Release:	3
License:	BSD-like (see COPYING)
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	7d852c49b74170cd662afabd86f40e8d
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	automake
BuildRequires:	xfce4-panel-devel >= 3.99.2
BuildRequires:	xmms
BuildRequires:	xmms-devel
Requires:	xfce4-panel >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which provide you control on XMMS from xfce4-panel.

%description -l pl
Wtyczka kt�ra umo�liwia kontrol� nad XMMS-em z pozycji panelu xfce.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/xmms-plugin
