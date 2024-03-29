<img src="./docs/media/estaty_logo.png" width="750"/>

[![Documentation Status](https://readthedocs.org/projects/estaty/badge/?version=latest)](https://estaty.readthedocs.io/en/latest/?badge=latest)

Module for spatial data fusion and processing for real estate objects.
**estaty** is Python-based platform to obtain and merge open spatial data with not very open and not very spatial to create “real estate use cases”.
Library provide tools for loaded data merging, pairwise source verification, proximity analysis, etc. 

## Installation

Use the following commands to install this module

Using pip:

```Bash
pip install estaty
```

Using poetry:

```Bash
poetry add estaty
```

## Documentation 

### Brief dive into spatial data processing

The variety of spatial data can be reduced to two large groups: raster and vector. 
Vector data can be presented as follows: point data, lines, polygons (Figure 1). So, 
**estaty** reduces completely all assimilated data to the following four types.

<img src="./docs/media/spatial_data.png" width="700"/>

Figure 1. Possible types of spatial data

The module thus downloads spatial data in just 
four formats (1 raster fields and 3 vector). The module is 
designed so that the most important parts are isolated from each other 
(multi-layer architecture). The DataSource layer is responsible for loading 
and generalising the data. So, there are exists the following 5 layers: 

- `DataSource`  - load and cache data,  reduce data to known and commonly used types;
- `Preprocessor` - preprocessing operation to prepare data for merging. For example, assign new CRS (re-projection);
- `Merger`  - merge raster and vector data if it is required;
- `Analyzer` - core of the system - use simple data representations and primitives to construct sequential analysis pipelines;
- `Report` - submodule for preparing PDF reports, data visualization and data send operations (for example POST request to desired service)

All above submodules can be flexibly configured to create custom data analysis pipelines:

<img src="./docs/media/arc_animation.gif" width="700"/>

## Usage examples 

Some use cases presented in a form of Python scripts - check [examples](./examples) folder for details.

## Cases 

<img src="https://raw.githubusercontent.com/wiredhut/estaty/main/docs/media/proximity_preview_berlin.png" width="700"/>

The service is designed to create a separate approaches for analysis (we call it use cases). All of them can be found in
the [cases folder](./cases):

* [area calculation](./cases/green_area) - example of using the library to compare areas
* [proximity analysis](./cases/proximity) - example of using the library to build routes to POIs (points of interest) of the required category and providing proximity analysis

Some release-related cases can be found via link [https://github.com/wiredhut/estaty_examples](https://github.com/wiredhut/estaty_examples)