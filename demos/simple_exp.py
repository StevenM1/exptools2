import sys
sys.path.append('exptools2')
from session import Session
from trial import Trial
from psychopy.visual import TextStim


class TestTrial(Trial):
    """ Simple trial with text (trial x) and fixation. """
    def __init__(self, session, trial_nr, phase_durations=None, verbose=True):
        super().__init__(session, trial_nr, phase_durations, verbose)

    def draw(self):
        """ Draws stimuli """
        if self.phase == 0:
            self.session.default_fix.draw()
        else:
            stim = TextStim(self.session.win, 'Trial %i' % (self.trial_nr))
            stim.draw()

        super().draw()


class TestSession(Session):
    """ Simple session with x trials. """
    def __init__(self, n_trials=10, eyetracker_on=False):
        """ Initializes TestSession object. """
        self.n_trials = n_trials
        super().__init__(eyetracker_on)

    def run(self):
        """ Runs experiment. """
        self.start_experiment()
        for trial_nr in range(self.n_trials):

            trial = TestTrial(
                session=self,
                trial_nr=trial_nr,
                phase_durations=(.5, .5),
                verbose=True
            )

            trial.run()
        self.close()


if __name__ == '__main__':

    session = TestSession(n_trials=2)
    session.run()