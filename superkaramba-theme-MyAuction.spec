%define		theme	MyAuction

Summary:	superkaramba - MyAuction theme
Summary(pl):	superkaramba - motyw MyAuction
Name:		superkaramba-theme-%{theme}
Version:	2.6
Release:        0.beta.2
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/15347-%{theme}.tar.gz
# Source0-md5:	a2cdfff3fae7edec931b18aeb621f279
Patch0:		myauction.py.patch
URL:		http://www.kde-look.org/content/show.php?content=15347
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyAuction lets you watch price and left time of auctions on internet
bidding platforms. Features:
- Configuration by interactive GUI menus (no script hacking required!)
- Features different platforms:
 - Ebay
 - Allegro.pl

%description -l pl
MyAuction pozwala na ogl±danie ceny i pozosta³ego czasu aukcji
internetowych. Mo¿liwo¶ci:
- Konfiguracja przez interaktywne menu GUI (nie jest wymagane rêczne
  modyfikowanie skryptów)
- Obs³ugiwane ró¿ne platformy:
 - Ebay
 - Allegro.pl

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}/{dev,img}

install %{theme}/dev/*.py $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}/dev
install %{theme}/img/*.* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}/img
install %{theme}/*.p* $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}
install %{theme}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/%{theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/%{theme}
