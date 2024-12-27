import subprocess


def copy(string, target=None):
    extra_args = []
    if target is not None:
        extra_args += ["-target", target]

    return subprocess.run(
        ["wl-copy"] + extra_args, universal_newlines=True, input=string
    )


def get(target=None):
    extra_args = []
    if target is not None:
        extra_args += ["-target", target]

    result = subprocess.run(
        ["wl-paste"] + extra_args, stdout=subprocess.PIPE, universal_newlines=True
    )

    # returncode = result.returncode
    stdout = result.stdout.strip()
    return stdout
