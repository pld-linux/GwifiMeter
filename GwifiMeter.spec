#TODO
# - build
Summary:	GwifiMeter
Summary(pl):	GwifiMeter
Name:		GwifiMeter
Version:	0.2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.gwifimeter.republika.pl/%{name}.src-%{version}.tar.gz
# Source0-md5:	dd390e5d3901fe917d4b221c32412c54
URL:		http://www.gwifimeter.republika.pl
BuildRequires:	gtk+2-devel >= 2:2.6.9
Requires:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
-

%description -l pl
Program jest interfejsem graficznym dla poleceñ z pakietu
wireless-tools, ifconfig, route, dhclient. Pozwala na zarz±dzanie
kartami wifi pod linuxem. Oprogramowanie powsta³o w oparciu o gtk2.

%prep
%setup -q -n %{name}

%build
%{__make}
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORIA README
