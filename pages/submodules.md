# Using Git sub modules

## Add a git submodule

	$ git add git submodule add -b main https://github.com/slug/repo.git mymodule 

## When cloning a repo containing submodules

	$ git clone https://github.com/slug/root.git
	$ cd root
	$ git submodule update --init

## Updating submodules

	$ git submodule update --remote


## References

[git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
