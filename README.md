# Strands Documentation

This package is used to generate documentation for the strands project in the
form of a readthedocs page.

## Installation

```sh
sudo apt-get install pandoc
pip install requests pypandoc
```

## Usage

Run

```sh
python scripts/doc_scraper.py
```

On the first run, an oauth header for github will be generated, which allows the
script to make more requests. By default only public repositories will be
scraped, but you can also scrape private repositories using the `--private` flag.
