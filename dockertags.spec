Name: dockertags
Version: 20150124
Release: 1%{?dist}
Summary: Get tags of a docker image from the index.docker.io.
License: Public Domain
URL: https://github.com/gashev/dockertags
Source0: https://github.com/gashev/dockertags/archive/master.zip
Packager: Oleg Gashev <oleg@gashev.net>
BuildArch: noarch
Requires: python-requests
%description
Get tags of a docker image from the index.docker.io.
%prep
%setup -q -n dockertags-master
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 dockertags $RPM_BUILD_ROOT/usr/bin/dockertags
%files
/usr/bin/dockertags
%changelog
* Sat Jan 24 2015 Oleg Gashev <oleg@gashev.net> - 20150124
- Initial package.
