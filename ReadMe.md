pysafetensors [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
==========
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/pysafetensors/workflows/CI/master/pysafetensors-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/pysafetensors/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/pysafetensors/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/pysafetensors.svg)](https://libraries.io/github/KOLANICH-libs/pysafetensors)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KFmts/pysafetensors (the namespace has changed to `KFmts`, which groups packages related to parsing or serialization), grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

A lib parsing [`safetensors` format](https://github.com/huggingface/safetensors) without involving Rust.

This parser relies on the [Kaitai Struct spec](https://codeberg.org/KFmts/kaitai_struct_formats/src/branch/safetensors/serialization/safetensors.ksy). And here are [the test files](https://codeberg.org/KOLANICH-datasets/kaitai_struct_samples/src/branch/safetensors/serialization/safetensors).

Currently undocumented, see the source code.
