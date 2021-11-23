from .particles import Particles, gen_local_particle_api, pmass
from .gaussian import generate_matched_gaussian_bunch
from .general import _pkg_root
from .build_particles import build_particles
from .linear_normal_form import compute_linear_normal_form
from .transverse_generators import generate_2D_polar_grid
from .transverse_generators import generate_2D_uniform_circular_sector
from .transverse_generators import generate_2D_pencil
from .transverse_generators import generate_2D_gaussian

def enable_pyheadtail_interface():
    import xpart.pyheadtail_interface.pyhtxtparticles as pp
    import xpart as xp
    xp.Particles = pp.PyHtXtParticles
