from estaty.analysis.stages.area import AreaAnalysisStage
from estaty.data_source.load.gbif_vector import LoadGBIFLocallyStage
from estaty.data_source.load.osm_vector import LoadOSMStage
from estaty.preprocessing.stages.project import VectorProjectionStage
from estaty.analysis.stages.distance import DistanceAnalysisStage
from estaty.stages import DummyStage


DATA_SOURCE_POOL_BY_NAME = {'osm': [LoadOSMStage],
                            'gbif_local': [LoadGBIFLocallyStage],
                            'reproject': VectorProjectionStage,
                            'distance': DistanceAnalysisStage,
                            'area': AreaAnalysisStage,
                            'dummy': DummyStage,
                            'stdout': None}
