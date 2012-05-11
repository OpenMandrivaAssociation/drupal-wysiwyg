%define modname		wysiwyg
%define drupal_version	7
%define module_version	2.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Wysywig module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
Requires:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
The Views module provides a flexible method for Drupal site designers
to control how lists and tables of content, users, taxonomy terms
and other data are presented.

This tool is essentially a smart query builder that, given enough information,
can build the proper query, execute it, and display the results. It has four
modes, plus a special mode, and provides an impressive amount of functionality
from these modes.

Among other things, Views can be used to generate reports, create summaries,
and display collections of images and other content.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc CHANGELOG.txt README.txt
