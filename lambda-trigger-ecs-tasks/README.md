Virtual environments in Python provide a solution to the problem of dependency conflicts. 
By default, all Python packages are installed into a single global namespace, which can cause compatibility issues 
between different projects on a single machine and make it difficult to resolve conflicts.

A virtual environment creates isolated Python environments to allow for different versions of Python and libraries to 
be used in separate projects, without interfering with each other.

This means that you can have multiple virtual environments on the same computer, each with its own set of packages, 
without them interfering with each other.


To create a new virtual environment, you can use the python -m venv command. 
For example, to create an environment named "myenv", you would run:

python -m venv myenv


To activate a virtual environment

source myenv/bin/activate

When the environment is activated, any Python scripts or commands run will use the version of Python and libraries 
within the virtualenv, rather than the system's global version.

To deactivate a virtual environment, simply type deactivate in the terminal.

pip install -e .





{
  "bucket_name": "trigger-ecs-tasks-120191",
  "file_key": "store_ranges.csv",
  "cluster_name": "test",
  "task_definition": "strore-specific-task"
}
