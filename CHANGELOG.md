# Changelog


## v0.1.0 (2019-07-05)

### New

* Implements `pyJWT` to produce auth tokens. [Diego Quintana]

  Read more in https://pyjwt.readthedocs.io/en/latest/

* Implements password attribute in user model with `flask-bcrypt` [Diego Quintana]

  - Implements flask-bcrypt with sane defaults for testing and developing
  (`BCRYPT_LOG_ROUNDS` parameter)
  - Adds a migration script for new column
  - Update former tests to support the password field
  - Adds tests that check for new exceptions

  Read more about `flask-bcrypt` in
  <https://github.com/maxcountryman/flask-bcrypt>

* Add tests against the previous migration, and refactor code into utils.py. [Diego Quintana]

* Enforce unique values in table users, add migration script. [Diego Quintana]

* Implements flask-migrate and initialize migrations with default settings. [Diego Quintana]

### Changes

* Change python base image used with docker (alpine -> slim) [Diego Quintana]

### Fix

* Improve clarity of migration scripts with alembic !db. [Diego Quintana]

  - Create an initial migration script, and adapt the former initial script to work as the follow up migrations
  - Enforce file names that are human readable, see <https://stackoverflow.com/questions/35672933/does-alembic-care-what-its-migration-files-are-called>


## v0.0.5 (2019-06-16)

### Changes

* Implement part argument on bump_version.sh and update makefile. [Diego Quintana]


## v0.0.4 (2019-06-15)

### New

* Sets client service to be served behind nginx container. [Diego Quintana]

* Add new container based on create-react-app, named as `client` [Diego Quintana]

* Add `AddUser` react form, tests and bump precommit hooks. [Diego Quintana]

* Update pre-commit with eslint support. [Diego Quintana]

* Add basic tests for the userlists component. [Diego Quintana]

### Changes

* Add testing dependencies. [Diego Quintana]

### Fix

* Fix insecure dependency axios, since 4786cf did not do it. [Diego Quintana]


## v0.0.3 (2019-06-02)

### New

* Adds short script to undo revision bump. [Diego Quintana]

* Implements flask-cors into the `users` service. [Diego Quintana]

* Add `refresh` task to `Makefile` [Diego Quintana]

  this recreates and seeds the db in one step.

* Implements flask-debugtoolbar in the application plus tests. [Diego Quintana]

  Read more about this flask extension in <https://flask-debugtoolbar.readthedocs.io/en/latest/>

### Changes

* Separates scripts for bumping version and changelog. [Diego Quintana]

  these both end up producing a CHANGELOG.md file, but I benefit from having `bump_changelog.sh` alone and then plugging it into the `bump_version.sh` script.

### Fix

* Fix broken call to `bump_changelog.sh` [Diego Quintana]

  it was overwriting `CHANGELOG.md` with an empty file

* Fixes security issue `axios`, updates library to `0.19.0` [Diego Quintana]

* `bump_version.sh` was running in dry-run mode. [Diego Quintana]


## v0.0.2 (2019-06-02)

### New

* Implements `bumpversion` and a script for updating versions. [Diego Quintana]

  the script is a workaround for <https://github.com/peritus/bumpversion/issues/137>

  Read more about `bumpversion` in <https://github.com/peritus/bumpversion/>

* Implements gitchangelog. [Diego Quintana]

  This helps in producing consistent changelogs. Read More in <https://github.com/vaab/gitchangelog>

* Add CHANGELOG.md and a VERSION file. [Diego Quintana]


## v0.0.1 (2019-06-01)

### New

* Add basic travis CI support. [Diego Quintana]

* Persist database data in a volume in compose. [Diego Quintana]

* Add dev requirements for pip, and implements python formatting tools. [Diego Quintana]

  this enforces the usage of black and flake8 using pre-commit git hooks,
  as described in
  <https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/>
  and provided by git `pre-commit` PyPi library at <https://github.com/pre-commit/pre-commit>

  Read more about python formatters in <https://medium.com/3yourmind/auto-formatters-for-python-8925065f9505>

* Add code coverage support. [Diego Quintana]

* Add a route and templates to the users service. [Diego Quintana]

* Add production dockerfiles and nginx container. [Diego Quintana]

* Add basic tests. [Diego Quintana]

* Add Dockerfiles and basic db service !docker !db. [Diego Quintana]

* First commit :tada: [Diego Quintana]

  add a single object available in `/users/ping` with `flask-restful`

### Changes

* Add `/users/all` and `/users/<id>` to api, plus tests. [Diego Quintana]

  also update `Makefile`

### Fix

* Remove volume directive from compose file. [Diego Quintana]


