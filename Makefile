all:
	pip install --editable .; pip install --editable .[dev]

test1:
	howfairis https://github.com/fair-software/howfairis

test2:
	howfairis https://github.com/bsipos/bsipos-conda

test3:
	howfairis https://github.com/pygame/pygame

test4:
	howfairis https://github.com/xtensor-stack/xtensor-fftw

test5:
	howfairis https://gitlab.com/gitlab-org/gitlab-foss

test6:
	howfairis https://gitlab.com/a.vijaykumar/bicgstab_l
