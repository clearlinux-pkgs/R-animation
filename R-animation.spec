#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-animation
Version  : 2.7
Release  : 32
URL      : https://cran.r-project.org/src/contrib/animation_2.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/animation_2.7.tar.gz
Summary  : A Gallery of Animations in Statistics and Utilities to Create
Group    : Development/Tools
License  : MIT
Requires: R-magick
BuildRequires : R-magick
BuildRequires : buildreq-R

%description
in probability theory, mathematical statistics, multivariate statistics,
    non-parametric statistics, sampling survey, linear models, time series,
    computational statistics, data mining and machine learning. These functions
    may be helpful in teaching statistics and data analysis. Also provided in this
    package are a series of functions to save animations to various formats, e.g.
    Flash, 'GIF', HTML pages, 'PDF' and videos. 'PDF' animations can be inserted
    into 'Sweave' / 'knitr' easily.

%prep
%setup -q -c -n animation
cd %{_builddir}/animation

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640887640

%install
export SOURCE_DATE_EPOCH=1640887640
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library animation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library animation
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library animation
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc animation || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/animation/CITATION
/usr/lib64/R/library/animation/DESCRIPTION
/usr/lib64/R/library/animation/INDEX
/usr/lib64/R/library/animation/Meta/Rd.rds
/usr/lib64/R/library/animation/Meta/data.rds
/usr/lib64/R/library/animation/Meta/demo.rds
/usr/lib64/R/library/animation/Meta/features.rds
/usr/lib64/R/library/animation/Meta/hsearch.rds
/usr/lib64/R/library/animation/Meta/links.rds
/usr/lib64/R/library/animation/Meta/nsInfo.rds
/usr/lib64/R/library/animation/Meta/package.rds
/usr/lib64/R/library/animation/NAMESPACE
/usr/lib64/R/library/animation/NEWS.md
/usr/lib64/R/library/animation/R/animation
/usr/lib64/R/library/animation/R/animation.rdb
/usr/lib64/R/library/animation/R/animation.rdx
/usr/lib64/R/library/animation/articles/jss725.Rnw
/usr/lib64/R/library/animation/articles/jss725.bib
/usr/lib64/R/library/animation/data/Rdata.rdb
/usr/lib64/R/library/animation/data/Rdata.rds
/usr/lib64/R/library/animation/data/Rdata.rdx
/usr/lib64/R/library/animation/demo/CLEvsLAL.R
/usr/lib64/R/library/animation/demo/IBM.R
/usr/lib64/R/library/animation/demo/Mandelbrot.R
/usr/lib64/R/library/animation/demo/Sierpinski.R
/usr/lib64/R/library/animation/demo/Sweave_animation.R
/usr/lib64/R/library/animation/demo/Xmas.R
/usr/lib64/R/library/animation/demo/Xmas2.R
/usr/lib64/R/library/animation/demo/Xmas_card.R
/usr/lib64/R/library/animation/demo/busybees.R
/usr/lib64/R/library/animation/demo/elephant.R
/usr/lib64/R/library/animation/demo/fire.R
/usr/lib64/R/library/animation/demo/fireworks.R
/usr/lib64/R/library/animation/demo/flowers.R
/usr/lib64/R/library/animation/demo/game_of_life.R
/usr/lib64/R/library/animation/demo/ggobi_animation.R
/usr/lib64/R/library/animation/demo/hanoi.R
/usr/lib64/R/library/animation/demo/jumpingHorse.R
/usr/lib64/R/library/animation/demo/lissajous.R
/usr/lib64/R/library/animation/demo/pollen.R
/usr/lib64/R/library/animation/demo/recur.leaf.R
/usr/lib64/R/library/animation/demo/recur.snow.R
/usr/lib64/R/library/animation/demo/recur.tree.R
/usr/lib64/R/library/animation/demo/rgl_animation.R
/usr/lib64/R/library/animation/demo/use_Cairo.R
/usr/lib64/R/library/animation/demo/wordrotation.R
/usr/lib64/R/library/animation/help/AnIndex
/usr/lib64/R/library/animation/help/aliases.rds
/usr/lib64/R/library/animation/help/animation.rdb
/usr/lib64/R/library/animation/help/animation.rdx
/usr/lib64/R/library/animation/help/paths.rds
/usr/lib64/R/library/animation/html/00Index.html
/usr/lib64/R/library/animation/html/R.css
/usr/lib64/R/library/animation/misc/ANI.css
/usr/lib64/R/library/animation/misc/FUN.js
/usr/lib64/R/library/animation/misc/Rweb/Rweb.R
/usr/lib64/R/library/animation/misc/Rweb/demo.html
/usr/lib64/R/library/animation/misc/Rweb/index.html
/usr/lib64/R/library/animation/misc/Sweave_animation.Rnw
/usr/lib64/R/library/animation/misc/animate/animate.sty
/usr/lib64/R/library/animation/misc/animate/animfp.sty
/usr/lib64/R/library/animation/misc/scianimator/MIT-LICENSE
/usr/lib64/R/library/animation/misc/scianimator/css/reset.css
/usr/lib64/R/library/animation/misc/scianimator/css/scianimator.blue.css
/usr/lib64/R/library/animation/misc/scianimator/css/scianimator.css
/usr/lib64/R/library/animation/misc/scianimator/css/scianimator.dark.css
/usr/lib64/R/library/animation/misc/scianimator/css/scianimator.light.css
/usr/lib64/R/library/animation/misc/scianimator/css/styles.css
/usr/lib64/R/library/animation/misc/scianimator/index.html
/usr/lib64/R/library/animation/misc/scianimator/js/jquery-1.4.4.min.js
/usr/lib64/R/library/animation/misc/scianimator/js/jquery.scianimator.min.js
/usr/lib64/R/library/animation/misc/scianimator/js/template.js
/usr/lib64/R/library/animation/tests/run-all.R
/usr/lib64/R/library/animation/tests/testit/utils.R
