import numpy as np

# Only patch what ember actually uses
np.int = int  # type: ignore[attr-defined]
np.float = float  # type: ignore[attr-defined]
np.complex = complex  # type: ignore[attr-defined]
np.str = str  # type: ignore[attr-defined]
np.object = object  # type: ignore[attr-defined]
# DO NOT patch np.bool — it breaks numpy.ma

import lief  # type: ignore[import-untyped]
import ember.features as ef  # type: ignore[import-untyped]

if not hasattr(lief, 'bad_format'):
    lief.bad_format = lief.lief_errors  # type: ignore[attr-defined]
if not hasattr(lief, 'bad_file'):
    lief.bad_file = lief.lief_errors  # type: ignore[attr-defined]
if not hasattr(lief, 'pe_error'):
    lief.pe_error = lief.lief_errors  # type: ignore[attr-defined]
if not hasattr(lief, 'parser_error'):
    lief.parser_error = lief.lief_errors  # type: ignore[attr-defined]
if not hasattr(lief, 'read_out_of_bound'):
    lief.read_out_of_bound = lief.lief_errors  # type: ignore[attr-defined]

def get_extractor():
    return ef.PEFeatureExtractor(2)