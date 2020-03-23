def pre_configure_hook(self, *args, **kwargs):
    """Hook to add SLURM support for OpenMPI."""
    if self.name == 'OpenMPI':
        self.log.info("[pre-configure hook] add SLURM support")
        self.cfg['configopts'] += ' --with-slurm --with-pmi '
