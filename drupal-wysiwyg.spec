%define modname		wysiwyg
%define drupal_version	7
%define module_version	2.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Wysywig module for Drupal
Version:	%{version}
Release:	2
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
Requires:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
Allows to use client-side editors to edit content. It simplifies
the installation and integration of the editor of your choice. This module
replaces all other editor integration modules. No other Drupal module is
required.

Wysiwyg module is capable to support any kind of client-side editor. It can be
a HTML-editor (a.k.a. WYSIWYG), a pseudo-editor (buttons to insert markup
into a textarea), or even Flash-based applications. The editor library needs
to be downloaded separately. Various editors are supported (see below).

Wysiwyg module also provides an abstraction layer for other Drupal modules
to integrate with any editor. This means that other Drupal modules can expose
content-editing functionality, regardless of which editor you have installed.

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


%changelog
* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.1-2
+ Revision: 798385
- fix description

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.1-1
+ Revision: 798293
- imported package drupal-wysiwyg

