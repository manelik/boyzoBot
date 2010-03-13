#ifndef SERVER_H
#define SERVER_H

namespace SERVER
{
        enum DEVICES { SMS, IM, NONE };
		
        enum RESP
		{
			OK = 200,
			NOT_MODIFIED = 304,
			BAD_REQUEST = 400,
			NOT_AUTHORIZED = 401,
			FORBIDDEN = 403,
			NOT_FOUND = 404,
			INTERNAL_SERVER_ERROR = 500,
			BAD_GATEWAY = 502,
			SERVICE_UNAVAILABLE = 503,
            UNKNOWN = 2723
		};
        
        struct Option1
        {
            Option1() { since="Tue%2C+22+Feb+2000+22%3A55%3A48+GMT"; sinceId=1; count=200; page=1; }
            /// Optional.  Narrows the returned results to just those statuses created after the specified HTTP-formatted date.
            QString since;
            /// Optional.  Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
            unsigned int sinceId;
            /// Optional.  Specifies the number of statuses to retrieve. May not be greater than 200.
            unsigned int count;
            /// Optional. Specify which page to return.
            unsigned int page;
        };

        struct Option2
        {
            Option2() { user=""; count=200; since="Tue%2C+22+Feb+2000+22%3A55%3A48+GMT"; sinceId=1; page=1; }
            /// Optional.  Specifies the ID or screen name of the user for whom to return the friends_timeline.
            QString user;
            /// Optional.  Specifies the number of statuses to retrieve. May not be greater than 200.
            unsigned int count;
            /// Optional.  Narrows the returned results to just those statuses created after the specified HTTP-formatted date.
            QString since;
            /// Optional.  Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
            unsigned int sinceId;
            /// Optional. Specify which page to return.
            unsigned int page;
        };
        
        struct Option3
        {
            Option3() { page=1; since="Tue%2C+22+Feb+2000+22%3A55%3A48+GMT"; sinceId=1; }
            /// Optional. Specify which page to return.
            unsigned int page;
            /// Optional.  Narrows the returned results to just those statuses created after the specified HTTP-formatted date.
            QString since;
            /// Optional.  Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
            unsigned int sinceId;
        };
        
        struct Option4
        {
            Option4() { user=""; page=1; lite=true; since="Tue%2C+22+Feb+2000+22%3A55%3A48+GMT"; }
            /// Optional.  The ID or screen name of the user for whom to request a list of friends.
            QString user;
            /// Optional. Specify which page to return.
            unsigned int page;
            /// Optional.  Prevents the inline inclusion of current status.  Must be set to a value of true.
            bool lite;
            /// Optional.  Narrows the returned results to just those statuses created after the specified HTTP-formatted date.
            QString since;
        };
        
        struct Option5
        {
            Option5() { user=""; page=1; lite=true; }
            /// Optional.  The ID or screen name of the user for whom to request a list of followers.
            QString user;
            /// Optional. Specify which page to return.
            unsigned int page;
            /// Optional.  Prevents the inline inclusion of current status.  Must be set to a value of true.
            bool lite;
        };
        
        struct Option6
        {
            Option6() { since="Tue%2C+22+Feb+2000+22%3A55%3A48+GMT"; sinceId=1; page=1; }
            /// Optional.  Narrows the returned results to just those statuses created after the specified HTTP-formatted date.
            QString since;
            /// Optional.  Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
            unsigned int sinceId;
            /// Optional. Specify which page to return.
            unsigned int page;
        };
};


#endif //SERVER_H
