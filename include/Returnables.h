#ifndef Returnables_H
#define Returnables_H

#include <QtCore/QLinkedList>
#include <QtCore/QMap>
#include "Server.h"

namespace Returnables
{
	struct User
	{
		unsigned int id;
		QString name;
		QString screenName;
		QString location;
		QString description;
		QString profileImageUrl;
		QString url;
		bool isProtected;
		unsigned int followersCount;
	};

	struct Details
	{
		QString profileBackgroundColor;
		QString profileTextColor;
		QString profileLinkColor;
		QString profileSidebarFillColor;
		QString profileSidebarBorderColor;
		unsigned int friendsCount;
		QString createdAt;
		unsigned int favoritesCount;
		int utcOffset;
		QString timeZone;
		QString profileBackgroundImageUrl;
		bool profileBackgroundTiled;
		unsigned int statusesCount;
	};

	struct Status
	{
		QString createdAt;
		unsigned int id;
		QString text;
		QString source;
		bool truncated;
		unsigned int inReplyToStatusId;
		unsigned int inReplyToUserId;
		bool favorited;
	};

	struct DirectHeader
	{
		unsigned int id;
		unsigned int senderId;
		QString text;
		unsigned int recipientId;
		QString createdAt;
		QString senderScreenName;
		QString recipientScreenName;
	};

	struct DirectMessage
	{
		DirectHeader headerInfo;
		User sender;
		User recipient;
	};

	struct StatusUser
	{
		Status status;
		User user;
	};

	enum RequestId { PUBLIC_TIMELINE, FRIENDS_TIMELINE, SINGLE_STATUS, FEATURED_USERS, LOGIN, \
					 TWITTER_UP, USER_TIMELINE, FAVORITES, NEW_STATUS, RECENT_REPLIES, REMOVE_STATUS, FRIENDS, \
					 FOLLOWERS, USER_DETAILS, SENT_DIRECT_MESSAGES, RECEIVED_DIRECT_MESSAGES, SEND_DIRECT_MESSAGE, \
					 REMOVE_DIRECT_MESSAGE, ADD_FRIENDSHIP, REMOVE_FRIENDSHIP, FRIENDSHIP_EXISTS, UPDATE_LOCATION, \
					 DELIVERY_DEVICE, API_REQUESTS, ADD_FAVORITE, REMOVE_FAVORITE, LOGOUT, VERIFY_CREDENTIALS };

	class Response
	{
		public:
			Response() {}
			virtual ~Response() {}
			RequestId reqID;
	};

	class FriendsTimeline : public Response
    {
		public:
			FriendsTimeline() {}
			~FriendsTimeline() {}
			QLinkedList<StatusUser*> list;
    };
	class PublicTimeline : public Response
	{
		public:
			PublicTimeline() {}
			virtual ~PublicTimeline() {}
			QLinkedList<StatusUser*> list;
	};
	class SingleStatus : public Response
	{
		public:
			SingleStatus() { status = new Returnables::Status(); user = new Returnables::User(); }
			virtual ~SingleStatus() { if(status) delete status; if(user) delete user; }
			Status* status;
			User* user;
	};
	class FeaturedUsers : public Response
	{
		public:
			FeaturedUsers() {}
			~FeaturedUsers() {}
			QLinkedList<StatusUser*> list;
	};
	class Login : public Response
	{
		public:
			Login() {}
			~Login() {}
			bool authorized;
	};
	class TwitterUp : public Response
	{
		public:
			TwitterUp() {}
			~TwitterUp() {}
			bool up;
	};
	class UserTimeline : public Response
	{
		public:
			UserTimeline() {}
			~UserTimeline() {}
			QLinkedList<StatusUser*> list;
	};
	class Favorites : public Response
	{
		public:
			Favorites() {}
			~Favorites() {}
			QLinkedList<StatusUser*> list;
	};
	class NewStatus : public Response
	{
		public:
			NewStatus() { newStatus = new Returnables::Status(); user = new Returnables::User(); }
			~NewStatus() { if(newStatus) delete newStatus; if(user) delete user; }
			Status* newStatus;
			User* user;
	};
	class RecentReplies : public Response
	{
		public:
			RecentReplies() {}
			~RecentReplies() {}
			QLinkedList<StatusUser*> list;
	};
	class RemoveStatus : public Response
	{
		public:
			RemoveStatus() { removedStatus = new Returnables::Status(); user = new Returnables::User(); }
			~RemoveStatus() { if(removedStatus) delete removedStatus; if(user) delete user; }
			Status *removedStatus;
			User *user;
	};
	class Friends : public Response
	{
		public:
			Friends() {}
			~Friends() {}
			QLinkedList<StatusUser*> list;
	};
	class Followers : public Response
	{
		public:
			Followers() {}
			~Followers() {}
			QLinkedList<StatusUser*> list;
	};
	class UserDetails : public Response
	{
		public:
			UserDetails() { user = new User(); details = new Details(); status = new Status(); }
			~UserDetails() { if(user) delete user; if(details) delete details; if(status) delete status; }
			User *user;
			Details *details;
			Status *status;
	};
	class SentDirectMessages : public Response
	{
		public:
			SentDirectMessages() {}
			~SentDirectMessages() {}
			QLinkedList<DirectMessage*> list;
	};
	class ReceivedDirectMessages : public Response
	{
		public:
			ReceivedDirectMessages() {}
			~ReceivedDirectMessages() {}
			QLinkedList<DirectMessage*> list;
	};
	class SendDirectMessage : public Response
	{
		public:
			SendDirectMessage() { headerInfo = new Returnables::DirectHeader(); sender = new Returnables::User(); recipient = new Returnables::User(); }
			~SendDirectMessage() { if(headerInfo) delete headerInfo; if(sender) delete sender; if(recipient) delete recipient; }
			DirectHeader *headerInfo;
			User *sender;
			User *recipient;
	};
	class RemoveDirectMessage : public Response
	{
		public:
			RemoveDirectMessage() { headerInfo = new Returnables::DirectHeader(); sender = new Returnables::User(); recipient = new Returnables::User(); }
			~RemoveDirectMessage() { if(headerInfo) delete headerInfo; if(sender) delete sender; if(recipient) delete recipient; }
			DirectHeader *headerInfo;
			User *sender;
			User *recipient;
	};
	class AddFriendship : public Response
	{
		public:
			AddFriendship() { user = new Returnables::User(); status = new Returnables::Status(); }
			~AddFriendship() { if(user) delete user; if(status) delete status; }
			User *user;
			Status *status;
	};
	class RemoveFriendship : public Response
	{
		public:
			RemoveFriendship() { user = new Returnables::User(); status = new Returnables::Status(); }
			~RemoveFriendship() { if(user) delete user; if(status) delete status; }
			User *user;
			Status *status;	
	};
	class FriendshipExist : public Response
	{
		public:
			FriendshipExist() {}
			~FriendshipExist() {}
			bool friends;
	};
	class UpdateLocation : public Response
	{
		public:
			UpdateLocation() { user = new Returnables::User(); status = new Returnables::Status(); }
			~UpdateLocation() { if(user) delete user; if(status) delete status; }
			User *user;
			Status *status;
	};
	class DeliveryDevice : public Response
	{
		public:
			DeliveryDevice() { user = new Returnables::User(); status = new Returnables::Status(); }
			~DeliveryDevice() { if(user) delete user; if(status) delete status; }
			User *user;
			Status *status;
	};
	class ApiRequests : public Response
	{
		public:
			ApiRequests() {}
			~ApiRequests() {}
			QString resetTime;
			unsigned int resetTimeSeconds;
			unsigned int remainingHits;
			unsigned int hourlyLimit;
	};
	class AddFavorite : public Response
	{
		public:
			AddFavorite() { status = new Returnables::Status(); user = new Returnables::User(); }
			~AddFavorite() { if(status) delete status; if(user) delete user; }
			Status *status;
			User *user;
	};
	class RemoveFavorite : public Response
	{
		public:
			RemoveFavorite() { status = new Returnables::Status(); user = new Returnables::User(); }
			~RemoveFavorite() { if(status) delete status; if(user) delete user; }
			Status *status;
			User *user;	
	};
};


#endif //Returnables_H
