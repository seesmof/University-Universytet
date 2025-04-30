from grapes.models import Bunch


def process_bunch(b: Bunch):
    if not b.outside and not b.shape and not b.color and not b.sugar and b.count>=100:
        b.stage=Bunch.Stage.Juice
    elif not b.outside and not b.shape and not b.color and not b.sugar:
        b.stage=Bunch.Stage.Wine
    elif not b.outside and not b.color and not b.sugar:
        b.stage=Bunch.Stage.Grapes
    elif not b.color and not b.sugar:
        b.stage=Bunch.Stage.Raisins
    else:
        b.stage=Bunch.Stage.Jelly
    
    return b