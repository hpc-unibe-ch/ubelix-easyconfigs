def parse_hook(self, *args, **kwargs):
    """Hook to add SLURM support for OpenMPI."""
    if self.name == 'OpenMPI':
        self.log.info("[parse hook] add SLURM support to OpenMPI")
        self['configopts'] += ' --with-slurm --with-pmix '

def parse_hook(self, *args, **kwargs):
    """Hook to add SLURM support for OpenMPI."""
    if self.name == 'impi':
        self.log.info("[parse hook] add SLURM support to IMPI")
        self['modextravars'] = {'I_MPI_PMI_LIBRARY': 'libpmi2.so'}
