Summary:	A simple TCP benchmarking utility
Summary(pl.UTF-8):   Proste narzędzie do pomiaru wydajności TCP
Name:		gensink
Version:	4.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://jes.home.cern.ch/jes/gensink/%{name}-%{version}.tar.gz
# Source0-md5:	82f029c4a450531ff44ad4eef6c38012
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gensink consists of a pair of utilities that measure the performance
of a TCP connection between two hosts.

%description -l pl.UTF-8
gensink składa się z pary narzędzi, które określają wydajność
połączenia TCP pomiędzy dwoma komputerami.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install gen4 sink4 tub4 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
