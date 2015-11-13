from app import db, models

def get_all_bugs():
    return models.Bug.query.all()
    
def add_bug(bug):
    db.session.add(bug)
    db.session.commit()
    
def get_bug(bug_id):
	return models.Bug.query.filter_by(id=bug_id).first()
    
def delete_bug(bug_id):
	bug = get_bug(bug_id)
	if bug:
		db.session.delete(bug)
		db.session.commit()
		return True
	else:
		return False
