# RELEASE

To create a release:

- Checkout from `dev` to `release/x.y.z`
- Update `VERSION` in [version.py](../src/zpa_demo/version.py) to `x.y.z`
- Update serverless version
  - `cd src/serverless && npm version x.y.z`
- Add a new entry to [CHANGELOG.md](./CHANGELOG.md)
  - Include date of release
  - Add features
  - Add changes
  - Add bug fixes
- Push branch
- Create PR to dev
- Create PR to master
