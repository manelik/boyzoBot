#ifndef QTWITLIB_H
#define QTWITLIB_H

#ifdef WIN32
	#define EXPORT __declspec(dllexport)
#else
	#define EXPORT
#endif

#include <QtCore/QString>
#include "Server.h"
#include "Core.h"

class QTwitLib : public Core
{
    public:
        EXPORT QTwitLib();
        virtual ~QTwitLib();
        
//=====================================================================
        // Unauthenticated Methods
//=====================================================================
        /**
         * Returns the 20 most recent statuses from non-protected users who have set a custom user icon.
         * Does not require authentication.
         */
        EXPORT void GetPublicTimeline();
//=====================================================================
        /**
         * Returns a single status, specified by the id parameter below.  The status's author will be returned inline.
         * @param id Required.  The numerical ID of the status you're trying to retrieve.
         */
        EXPORT void GetSingleStatus(unsigned int id);
//=====================================================================
        /**
         * Returns a list of the users currently featured on the site with their current statuses inline.
         */
        EXPORT void GetFeaturedUsers();
//=====================================================================
        /**
         * Ends the session of the authenticating user, returning a null cookie.
         * Use this method to sign users out of client-facing applications like widgets.
         */
        EXPORT void Logout();
//=====================================================================
        /**
         * Attempts to establish an authorized connection with Twitter.
         */
        EXPORT void Login(QString user, QString password);
//=====================================================================
        /**
         * Returns the string "ok" in the requested format with a 200 OK HTTP status code.
         */
        EXPORT void IsTwitterUp();
//=====================================================================
//=====================================================================


//=====================================================================
        // Authenticated/Unauthenticated Methods
//=====================================================================
        /**
         * Returns the 20 most recent statuses posted from the authenticating user.
         * It's also possible to request another user's timeline via the id parameter below.
         * This is the equivalent of the Web /archive page for your own user, or the profile page for a third party.
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetUsersTimeline(SERVER::Option2 *opt=NULL);
//=====================================================================
        /**
         * Returns the 20 most recent favorite statuses for the authenticating user or user specified by the ID parameter in the requested format.
         * @param user Optional.  The ID or screen name of the user for whom to request a list of favorite statuses.
         */
        EXPORT void GetFavorites(QString user="", unsigned int page=1);
//=====================================================================
//=====================================================================


//=====================================================================
        // Authenticated Methods
//=====================================================================
        /**
         * Returns the 20 most recent statuses posted by the authenticating user and that user's friends.
         * This is the equivalent of /home on the Web. 
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetFriendsTimeline(SERVER::Option1 *opt=NULL);
//=====================================================================
        /**
         * Updates the authenticating user's status.  Requires the status parameter specified below.  Request must be a POST.
         * @param status Required.  The text of your status update.  Be sure to URL encode as necessary.
         * Must not be more than 160 characters and should not be more than 140 characters to ensure optimal display.
         */
        EXPORT void PostNewStatus(QString status);                                                
//=====================================================================
        /**
         * Returns the 20 most recent @replies (status updates prefixed with @username) for the authenticating user.
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetRecentReplies(SERVER::Option3 *opt=NULL); 
//=====================================================================
        /**
         * Destroys the status specified by the required ID parameter.  The authenticating user must be the author of the specified status.
         * @param id Required.  The ID of the status to destroy.
         */
        EXPORT void RemoveStatus(unsigned int id);
//=====================================================================
        /**
         * Returns up to 100 of the authenticating user's friends who have most recently updated, each with current status inline.
         * It's also possible to request another user's recent friends list via the id parameter below.
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetFriends(SERVER::Option4 *opt=NULL);
//=====================================================================
        /**
         * Returns the authenticating user's followers, each with current status inline.
         * They are ordered by the order in which they joined Twitter (this is going to be changed).
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetFollowers(SERVER::Option5 *opt=NULL);
//=====================================================================
        /**
         * Returns extended information of a given user, specified by ID or screen name as per the required id parameter below.
         * This information includes design settings, so third party developers can theme their widgets according to a given user's preferences.
         * You must be properly authenticated to request the page of a protected user.
         * @param user Required.  The ID or screen name of a user.
         */
        EXPORT void GetUserDetails(QString user);
//=====================================================================
        /**
         * Returns a list of the 20 most recent direct messages sent by the authenticating user.
         * The XML and JSON versions include detailed information about the sending and recipient users.
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetSentDirectMessages(SERVER::Option6 *opt=NULL);
//=====================================================================
        /**
         * Returns a list of the 20 most recent direct messages sent to the authenticating user.  
         * The XML and JSON versions include detailed information about the sending and recipient users.
         * @param opt Optional.  Options which can be user specified.
         */
        EXPORT void GetReceivedDirectMessages(SERVER::Option6 *opt=NULL);;
//=====================================================================
        /**
         * Sends a new direct message to the specified user from the authenticating user.
         * Requires both the user and text parameters below.  Request must be a POST.
         * Returns the sent message in the requested format when successful.
         * @param user Required.  The ID or screen name of the recipient user.
         * @param text Required.  The text of your direct message.
         * Be sure to URL encode as necessary, and keep it under 140 characters.
         */
        EXPORT void SendDirectMessage(QString user, QString text);
//=====================================================================
        /**
         * Destroys the direct message specified in the required ID parameter.
         * The authenticating user must be the recipient of the specified direct message.
         * @param id Required.  The ID of the direct message to destroy.
         */
        EXPORT void RemoveDirectMessage(unsigned int id);
//=====================================================================
        /**
         * Befriends the user specified in the ID parameter as the authenticating user.
         * Returns the befriended user in the requested format when successful.
         * Returns a string describing the failure condition when unsuccessful.
         * @param user Required.  The ID or screen name of the user to befriend.
         */
        EXPORT void AddFriendship(QString user, bool follow=true);
//=====================================================================
        /**
         * Discontinues friendship with the user specified in the ID parameter as the authenticating user.
         * Returns the un-friended user in the requested format when successful.  Returns a string describing the failure condition when unsuccessful.
         * @param user Required.  The ID or screen name of the user with whom to discontinue friendship.
         */
        EXPORT void RemoveFriendship(QString user);
//=====================================================================
        /**
         * Tests if a friendship exists between two users.
         * @param user_a Required.  The ID or screen_name of the first user to test friendship for.
         * @param user_b Required.  The ID or screen_name of the second user to test friendship for.
         */
        EXPORT void FriendshipExist(QString user_a, QString user_b);
//=====================================================================
        /**
         * Returns an HTTP 200 OK response code and a format-specific response if authentication was successful.
         * Use this method to test if supplied user credentials are valid with minimal overhead.
         */
        EXPORT void VerifyCredentials();
//=====================================================================
        /**
         * Updates the location attribute of the authenticating user, as displayed on the side of their profile and returned in various API methods.
         * Works as either a POST or a GET.
         * @param location Required.  The location of the user.  Please note this is not normalized, geocoded, or translated to latitude/longitude at this time.
         */
        EXPORT void UpdateLocation(QString location);
//=====================================================================
        /**
         * Sets which device Twitter delivers updates to for the authenticating user.
         * Sending none as the device parameter will disable IM or SMS updates.
         * @param device Required.  Must be one of: sms, im, none.
         */
        EXPORT void UpdateDeliveryDevice(SERVER::DEVICES device);
//=====================================================================
        /**
         * Returns the remaining number of API requests available to the authenticating user before the API limit is reached for the current hour.
         * Calls to rate_limit_status require authentication, but will not count against the rate limit.
         */
        EXPORT void RemainingApiRequests();
//=====================================================================
        /**
         * Favorites the status specified in the ID parameter as the authenticating user.  Returns the favorite status when successful.
         * @param id  Required.  The ID of the status to favorite.
         */
        EXPORT void AddFavorite(unsigned int id);
//=====================================================================
        /**
         * Un-favorites the status specified in the ID parameter as the authenticating user.
         * Returns the un-favorited status in the requested format when successful.
         * @param id Required.  The ID of the status to un-favorite.
         */
        EXPORT void RemoveFavorite(unsigned int id);
//=====================================================================   
};


#endif // TWITLIB_H
