from pydra.engine.specs import ShellOutSpec, ShellSpec, SpecInfo

from pydra import ShellCommandTask

__all__ = ("GTMSeg",)

gtmseg_input_fields = [
    (
        "subject",
        str,
        {
            "help_string": "subject to analyze",
            "argstr": "--s {subject}",
            "mandatory": True,
        },
    ),
    (
        "output_volume",
        str,
        {
            "help_string": "output volume relative to subject/mri directory",
            "argstr": "--o {output_volume}",
        },
    ),
    (
        "headseg",
        str,
        {
            "help_string": "custom headseg",
            "argstr": "--head {headseg}",
        }
    ),
    (
        "colortable",
        str,
        {
            "help_string": "custom colortable",
            "argstr": "--ctab {colortable}",
        },
    ),
    (
        "upsampling_factor",
        float,
        {
            "help_string": "upsampling factor",
            "argstr": "--usf {upsampling_factor}",
        },
    ),
    (
        "output_upsampling_factor",
        float,
        {
            "help_string": "output upsampling factor (if different than upsampling factor)",
            "argstr": "--output-usf {output_upsampling_factor}",
        },
    ),
    (
        "keep_hypointensities",
        bool,
        {
            "help_string": "do not relabel hypointensities as WM",
            "argstr": "--keep-hypo",
        },
    ),
    (
        "keep_corpus_callosum",
        bool,
        {
            "help_string": "do not relabel corpus callosum as WM",
            "argstr": "--keep-cc",
        },
    ),
    (
        "subsegment_wm",
        bool,
        {
            "help_string": "subsegment WM into lobes",
            "argstr": "--subsegwm",
        },
    ),
]

gtmseg_input_spec = SpecInfo(
    name="GTMSegInputSpec",
    fields=gtmseg_input_fields,
    bases=(ShellSpec,),
)

gtmseg_output_fields = []

gtmseg_output_spec = SpecInfo(
    name="GTMSegOutputSpec",
    fields=gtmseg_output_fields,
    bases=(ShellOutSpec,),
)


class GTMSeg(ShellCommandTask):
    """Task for FreeSurfer's gtmseg.

    Examples
    --------
    >>> task = GTMSeg(subject="subject")
    >>> task.cmdline
    'gtmseg --s subject'
    >>> task = GTMSeg(
    ...     subject="subject",
    ...     keep_hypointensities=True,
    ...     subsegment_wm=True,
    ...     output_volume="gtmseg.wmseg.hypo.mgz",
    ...     upsampling_factor=1,
    ... )
    >>> task.cmdline
    'gtmseg --s subject --o gtmseg.wmseg.hypo.mgz --usf 1 --keep-hypo --subsegwm'
    >>> task = GTMSeg(
    ...     subject="subject",
    ...     output_volume="gtmseg+myseg.mgz",
    ...     headseg="apas+head+myseg.mgz",
    ...     colortable="myseg.colortable.txt",
    ... )
    >>> task.cmdline
    'gtmseg --s subject --o gtmseg+myseg.mgz --head apas+head+myseg.mgz --ctab myseg.colortable.txt'
    """

    input_spec = gtmseg_input_spec
    output_spec = gtmseg_output_spec
    executable = "gtmseg"