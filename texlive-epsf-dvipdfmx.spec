Name:		texlive-epsf-dvipdfmx
Version:	35575
Release:	2
Summary:	Plain TeX file for using epsf.tex with (x)dvipdfmx
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epsf-dvipdfmx
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf-dvipdfmx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf-dvipdfmx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
epsf-dvipdfmx.tex is a plain TeX file to be \input after
epsf.tex when using plain TeX with dvipdfmx. As in: \input epsf
\input epsf-dvipdfmx It is needed when an .eps file has
anything except the origin (0,0) for the lower-left of its
bounding box.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/epsf-dvipdfmx
%doc %{_texmfdistdir}/doc/plain/epsf-dvipdfmx

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
