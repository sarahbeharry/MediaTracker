from app import db, models


def get_all_tags():
    return models.Tag.query.all()


def get_tag(tag_id):
    return models.Tag.query.filter_by(id=tag_id).first()


def add_tag(tag):
    db.session.add(tag)
    db.session.commit()


def update_tag(tag):
    db.session.merge(tag)
    db.session.commit()


def delete_tag(tag_id):
    tag = get_tag(tag_id)
    if tag:
        tag.tagged_media = []
        db.session.merge(tag)
        db.session.delete(tag)
        db.session.commit()
        return True
    else:
        return False


def edit_tag(tag_id, name, colour, style, description):
    tag = get_tag(tag_id)
    if tag:
        tag.name = name
        tag.colour = colour
        tag.style = style
        tag.description = description
        update_tag(tag)


def convert_to_tags(tag_list_id):
    return models.Tag.query.filter(models.Tag.id.in_(tag_list_id)).all()
