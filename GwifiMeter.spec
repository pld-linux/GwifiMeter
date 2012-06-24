# TODO:
# - good patch for user path - calback.c line 178- man getpwuid
# - optflags
Summary:	GwifiMeter - frontend GUI for wireless-tools
Summary(de.UTF-8):   GwifiMeter - ein GUI für wireless-tools
Summary(pl.UTF-8):   GwifiMeter - interfejs graficzny dla wireless-tools
Name:		GwifiMeter
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.gwifimeter.republika.pl/%{name}.src-%{version}.tar.gz
# Source0-md5:	dd390e5d3901fe917d4b221c32412c54
Patch0:		%{name}-user_path.patch
URL:		http://www.gwifimeter.republika.pl
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
%setup -q -n %{name}
%patch0 -p1

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
