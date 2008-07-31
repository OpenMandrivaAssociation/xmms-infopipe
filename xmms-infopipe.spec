%define name    xmms-infopipe
%define version 1.3

Name:           %{name}
Version:    %{version}
Release:    %mkrel 6
Summary:    XMMS plugin that report XMMS status via a named pipe
License:    GPL
Group:      Sound
Source:     http://www.beastwithin.org/users/wwwwolf/code/xmms/%{name}-%{version}.tar.bz2
URL:        http://www.beastwithin.org/users/wwwwolf/code/xmms/infopipe.html
BuildRequires: xmms-devel >= 1.0.0
Buildroot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
XMMS InfoPipe is a plugin that reports XMMS status via named pipe. 
Handy if you want to add interesting real-time information for a personal 
web page, or a web cam page.

%prep
%setup -q

%build
%configure2_5x
%make
perl -pi -e 's/\$input = fread \(\$info, 261\);/\$input = fread (\$info, 2048);/' applications/xmms-info.php

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xmms/General/
mv src/.libs/libinfopipe-1.3.so.1.0.1 $RPM_BUILD_ROOT%{_libdir}/xmms/General/libinfopipe.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%doc applications/{lirc-say.pl,xmms-info.php,xmms-info.pl}
%{_libdir}/xmms/General/*

