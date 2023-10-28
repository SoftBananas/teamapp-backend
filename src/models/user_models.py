from sqlalchemy import Column, VARCHAR, Integer

from config.database import Base, metadata


class User(Base):
    __tablename__ = "user"
    metadata = metadata
    uuid = Column(UUID, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    lastname = Column(VARCHAR, nullable=False)
    username = Column(VARCHAR, nullable=False)
    mail = Column(VARCHAR, nullable=False)
    hashed_password = Column(VARCHAR, nullable=False)
    is_verified = Column(BOOL, nullable=False)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    image = Column(VARCHAR, nullable=True)
    location = Column(JSON, nullable=True)
    sex = Column(VARCHAR, nullable=True)
    birthday = Column(DATE, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)
    is_blocked = Column(BOOL, nullable=False)


class CV(Base):
    __tablename__ = "cv"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, nullable=False)
    description = Column(VARCHAR, nullable=True)


class CV_Contact(Base):
    __tablename__ = "cv_contact"
    metadata = metadata
    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    contact_id = Column(Integer, ForeignKey(Contact_Type.id), primary_key=True)
    contact_data = Column(VARCHAR, nullable=True)
    is_preferred = Column(BOOL, nullable=True)


class Contact_Type(Base):
    __tablename__ = "contact_type"
    metadata = metadata
    id = Column(UUID, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Role(Base):
    __tablename__ = "role"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Education(Base):
    __tablename__ = "education"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)
    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)


class Exrerience(Base):
    __tablename__ = "exrerience"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    cv_id = Column(Integer, ForeignKey(CV.id), nullable=False)
    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=False)
    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)


class Notification(Base):
    __tablename__ = "notification"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    image = Column(Integer, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    title = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)


#SETTINGS MODULE
class Settings(Base):
    __tablename__ = "settings"
    metadata = metadata
    user_id = Column(UUID, ForeignKey(User.uuid), primary_key=True)
    is_notifying = Column(BOOL, nullable=True)
    is_mailing = Column(BOOL, nullable=True)


class Privacy(Base):
    __tablename__ = "privacy"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class User_Privacy(Base):
    __tablename__ = "user_privacy"
    metadata = metadata
    user_id = Column(UUID, primary_key=True)
    privacy_id = Column(Integer, primary_key=True)


#SKILL MODULE

class CV_Skill(Base):
    __tablename__ = "cv_skill"
    metadata = metadata
    cv_id = Column(Integer, ForeignKey(CV.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)


class Skill(Base):
    __tablename__ = "skill"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Speciality(Base):
    __tablename__ = "speciality"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)


class AD_Skill(Base):
    __tablename__ = "ad_skill"
    metadata = metadata
    ad_id = Column(Integer, ForeignKey(AD.id), primary_key=True)
    skill_id = Column(Integer, ForeignKey(Skill.id), primary_key=True)


#SUBSCRIPTION MODULE

class Subscription(Base):
    __tablename__ = "subscription"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    subscription_id = Column(Integer, ForeignKey(Subscription_type.id), nullable=False)
    date_start = Column(DATE, nullable=True)
    date_end = Column(DATE, nullable=False)
    payment = Column(Float, nullable=False)
    currency_id = Column(Integer, nullable=False)

class Currency(Base):
    __tablename__ = "currency"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Subscription_type(Base):
    __tablename__ = "subscription_type"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=False)
    max_response_count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    currency_id = Column(Integer, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Sale(Base):
    __tablename__ = "sale"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR, nullable=False) #разве нот нал
    date_start = Column(DATE, nullable=True)
    date_end = Column(DATE, nullable=False)
    percent = Column(Integer, nullable=False)
    subscription_id = Column(Integer, ForeignKey(Subscription_type.id), nullable=False)


#TEAM MODULE

class Team(Base):
    __tablename__ = "team"
    metadata = metadata
    uuid = Column(UUID, primary_key=True)
    owner_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    name = Column(VARCHAR, nullable=False)
    image = Column(VARCHAR, nullable=True)
    description = Column(TEXT, nullable=True)
    member_description = Column(TEXT, nullable=True)
    privacy = Column(JSON, nullable=True) # непанятна
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)


class User_team(Base):
    __tablename__ = "user_team"
    metadata = metadata
    user_id = Column(UUID, ForeignKey(User.uuid), nullable=False)
    team_id = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    speciality = Column(VARCHAR, nullable=True)


class Team_role(Base):
    __tablename__ = "team_role"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    team_id = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    name = Column(VARCHAR, nullable=False)


class Team_role_permission(Base):
    __tablename__ = "team_role_permission"
    metadata = metadata
    role_id = Column(Integer, ForeignKey(Team_role.id), primary_key=True)
    permission_id = Column(Integer, ForeignKey(Team_permission.id), primary_key=True)
    value = Column(BOOL, nullable=False)


class Team_permission(Base):
    __tablename__ = "team_permission"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)


class Exrerience(Base):
    __tablename__ = "exrerience"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    team_id = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    date_from = Column(DATE, nullable=True)
    date_to = Column(DATE, nullable=False)
    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)


class AD(Base):
    __tablename__ = "ad"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    team_id = Column(UUID, ForeignKey(Team.uuid), nullable=False)
    speciality = Column(VARCHAR, nullable=True)
    name = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=True)
    is_hide = Column(BOOL, nullable=False)
    is_promoting = Column(BOOL, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)


#CHAT MODULE

class Chat(Base):
    __tablename__ = "chat"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    chat_name = Column(VARCHAR, nullable=False)
    image = Column(VARCHAR, nullable=True)
    created_at = Column(DATETIME, nullable=False)


class Chat_member(Base):
    __tablename__ = "chat_member"
    metadata = metadata
    chat_id = Column(Integer, ForeignKey(Chat.id), primary_key=True)
    entity_id = Column(Integer, primary_key=True)
    created_at = Column(DATETIME, nullable=False)


class Message(Base):
    __tablename__ = "message"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey(Chat.id), nullable=False)
    member_id = Column(Integer, ForeignKey(Chat_member.id), nullable=False)
    text = Column(TEXT, nullable=True)
    created_at = Column(DATETIME, nullable=False)
    updated_at = Column(DATETIME, nullable=False)
    deleted_at = Column(DATETIME, nullable=True)


class Massage_image(Base):
    __tablename__ = "massage_image"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    massage_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    image_url = Column(VARCHAR, nullable=False)


class Massage_file(Base):
    __tablename__ = "massage_file"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    massage_id = Column(Integer, ForeignKey(Message.id), nullable=False)
    file_url = Column(VARCHAR, nullable=False)


class Massage_response(Base):
    __tablename__ = "massage_response"
    metadata = metadata
    massage_id = Column(Integer, ForeignKey(Message.id), primary_key=True)
    response_id = Column(Integer, ForeignKey(AD_response.id), primary_key=True)


#RESPONSE MODULE

class AD_response(Base):
    __tablename__ = "ad_response"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID, nullable=False)
    ad_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)


class CV_response(Base):
    __tablename__ = "ad_response"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    team_id = Column(UUID, nullable=False)
    cv_id = Column(Integer, nullable=False)
    status_id = Column(Integer, nullable=False)


class Response_status(Base):
    __tablename__ = "response_status"
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    slug = Column(VARCHAR, nullable=False)