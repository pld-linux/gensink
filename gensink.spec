Summary: A simple TCP benchmarking utility
Name: gensink
Version: 4.1
Release: 1
Copyright: GPL
Group: Applications/Internet
Source0: http://home.cern.ch/~jes/gensink-4.1.tar.gz
BuildRoot: /var/tmp/gensink-%{version}

%description
gensink consists of a pair of utilities that measure the performance of
a TCP connection between two hosts.

%prep
%setup 
 
%build
make

%install

mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 755 gen4 $RPM_BUILD_ROOT/usr/sbin/gen4
install -m 755 sink4 $RPM_BUILD_ROOT/usr/sbin/sink4
install -m 755 tub4 $RPM_BUILD_ROOT/usr/sbin/tub4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/sbin/gen4
/usr/sbin/sink4
/usr/sbin/tub4
%changelog
* Wed May 16 2001 Jes Sorensen <jes@trained-monkey.org>
- Bumped to 4.1
* Mon Mar 12 2001 Sandro Mazzucato <sandro@zeroknowledge.com>
- Added tub4
* Sat Oct 14 2000 Zach Brown <zab@zabbo.net>
- first pass
