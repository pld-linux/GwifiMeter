Summary:	GwifiMeter - frontend GUI for wireless-tools
Summary(de):	GwifiMeter - ein GUI für wireless-tools
Summary(pl):	GwifiMeter - interfejs graficzny dla wireless-tools
Name:		GwifiMeter
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.gwifimeter.republika.pl/%{name}.src-%{version}.tar.gz
# Source0-md5:	dd390e5d3901fe917d4b221c32412c54
URL:		http://www.gwifimeter.republika.pl
BuildRequires:	gtk+2-devel >= 2:2.6.9
BuildRequires:	pkgconfig
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application is a frontend GUI for wireless-tools, ifconfig,
route, dhclient. It uses gtk2 and makes wifi managing much easier.

%description -l de
Dieses Programm ist ein GUI für wireless-tools, ifconfig, route,
dhclient. Es benutzt gtk2 und ermöglicht eine viel enifachere wifi
Verwaltung.

%description -l pl
Program jest interfejsem graficznym dla poleceñ z pakietu
wireless-tools, ifconfig, route, dhclient. Pozwala na zarz±dzanie
kartami wifi pod linuxem. Oprogramowanie powsta³o w oparciu o gtk2.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORIA README profile-example
%attr(755,root,root) %{_bindir}/%{name}
