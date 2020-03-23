import abc


class ProjectSummary(metaclass=abc.ABCMeta):
    def __init__(self, name, base, total_batches, completed_batches, total_jobs, completed_jobs,
                 total_frames, completed_frames, annotations):
        self.name = name
        self.base = base
        self.total_batches = total_batches
        self.completed_batches = completed_batches
        self.total_jobs = total_jobs
        self.completed_jobs = completed_jobs
        self.total_frames = total_frames
        self.completed_frames = completed_frames
        self.annotations = annotations

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'base') and
                callable(subclass.base) and
                hasattr(subclass, 'total_batches') and
                callable(subclass.total_batches) and
                hasattr(subclass, 'completed_batches') and
                callable(subclass.completed_batches) and
                hasattr(subclass, 'total_jobs') and
                callable(subclass.total_jobs) and
                hasattr(subclass, 'completed_jobs') and
                callable(subclass.completed_jobs) and
                hasattr(subclass, 'total_frames') and
                callable(subclass.total_frames) and
                hasattr(subclass, 'completed_frames') and
                callable(subclass.completed_frames) and
                hasattr(subclass, 'annotations') and
                callable(subclass.annotations)
                )
