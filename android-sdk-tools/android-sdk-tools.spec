%define debug_package %{nil}
%define upstream_name tools
%define upstream_ver 3859397
%define install_dir_name %{upstream_name}
%define _install_prefix /opt/android

Name: sdk-tools
Summary: Android sdk tools for sdkmanager.
Version: %{upstream_ver}
Release: 26.0.2
License: ???
Group: Android
Source0: https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
Source1: android-tools.sh
BuildRequires: java
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-XXXXXX)
AutoReqProv: no

%description
%{name}

%prep
%setup -q -n tools

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{_install_prefix}/%{install_dir_name}
cp -a * %{buildroot}/%{_install_prefix}/%{install_dir_name}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/android-tools.sh

%clean
rm -fr %{buildroot}

%files
%defattr(-, root, root)
%{_sysconfdir}/profile.d/android-tools.sh
%{_install_prefix}/%{install_dir_name}
