
%define		_name	gwifimeter

Summary:	GwifiMeter - frontend GUI for wireless-tools
Summary(de.UTF-8):	GwifiMeter - ein GUI für wireless-tools
Summary(pl.UTF-8):	GwifiMeter - interfejs graficzny dla wireless-tools
Name:		GwifiMeter
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.gwifimeter.republika.pl/download/%{name}.src-%{version}.tar.gz
# Source0-md5:	0094ac51e76436b81ef6133b4d00e0be
URL:		http://www.gwifimeter.republika.pl/
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.6.9
BuildRequires:	pkgconfig
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application is a frontend GUI for wireless-tools, ifconfig,
route, dhclient. It uses GTK+2 and makes WiFi managing much easier.

%description -l de.UTF-8
Dieses Programm ist ein GUI für wireless-tools, ifconfig, route,
dhclient. Es benutzt GTK+2 und ermöglicht eine viel enifachere WiFi
Verwaltung.

%description -l pl.UTF-8
Program jest interfejsem graficznym dla poleceń z pakietu
wireless-tools, ifconfig, route, dhclient. Pozwala na zarządzanie
kartami WiFi pod Linuksem. Oprogramowanie powstało w oparciu o GTK+2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install pixmaps/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{_name}/themes/app
rm -rf $RPM_BUILD_ROOT/usr/doc/%{_name}

%find_lang %{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{_name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
