# Strands Documentation

This package is used to generate documentation for the strands project in the
form of a readthedocs page.

## Installation

```sh
sudo apt-get install pandoc
pip install requests pypandoc
```

## Usage

The `doc_scraper.py` script is used to scrape documentation from specified github
repositories and dataset webpages. It is only necessary to run this if the documentation
in one of those locations has changed. You don't need to run it if you're just
making changes in this repository.

```sh
python scripts/doc_scraper.py
```

On the first run, an oauth header for github will be generated, which allows the
script to make more requests. By default only public repositories will be
scraped, but you can also scrape private repositories using the `--private` flag.

The script will then download all repositories in the organisation, excluding
those specified in `conf/conf.yaml`. You can also exclude readme files which
match specific strings on a per-repository basis, by adding a list below the
repo name in the `ignore_repos` list.

For example, the following would ignore the whole `strands_utils` repository

```yaml
ignore_repos:
  - strands_utils
```

But this would only ignore files which contain the string `trash_file` or `bad_readme`

```yaml
ignore_repos:
  - strands_utils:
    - trash_file
	- bad_readme
```

You can use a different config by passing a
file to the `--conf` flag, which should contain the same keys that the one in
the `conf` directory has. Packages with a wiki page will also have those cloned
and added to the docs directory. You can ignore wikis using the `--nowiki` flag.

With the `--datasets` flag, the scraper will go through dataset urls given in
`datasets/datasets.yaml` and download the html pages specified there, converting
them to markdown. Images on the pages will also be downloaded to the
`datasets/images` directory.

The documentation is monitored by readthedocs, and any changes in the master branch
should be visible on the website after a short time.
