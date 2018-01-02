MIN_LENGTH = 1
MAX_LENGTH = 140
def is_valid_tweet(tweet):
    """ (str) -> bool

    Return True if and only if tweet is no less than 1 and no more 
    than 140 characters long.

    >>> is_valid_tweet('To me programming is more than an important ' \
              + 'practical art. It is also a gigantic undertaking in the ' \
              + 'foundations of knowledge. - Grace Hoptweet is no less than 1
              and no more than 140 characters longper')
    True
    >>> is_valid_tweet('The best programs are written so that computing ' \
             + 'machines can perform them quickly and so that human beings can
             ' \ + 'understand them clearly. - Donald Knuth')
    False
    """
    if   MIN_LENGTH <= len(tweet) <= MAX_LENGTH :
        return True
    else:
        return False


def contains_hash_symbol(tweet):
    """  (str) -> bool

    Return True if the tweet contains a hash symbol( tweet is no less than 1 and
    no more than 140 characters long).

    >>>contains_has h_symbol( '#bangerztour SOUTH AMERICA http://instagram.
             com/p/ s2IbhHQzGC/')
    True
    >>>contains_hash_symbol('Just posted a photo http://instagram.com/p/tCV
             xWaQzI4 / ')
    False
    """
    if '#' in tweet:
        return True
    else:
        return False


def is_mentioned( tweet, username ):
    """ ( str ,  str ) -> bool

    Return True if and only if the tweet includes a username preceded by the
    character @. ( tweet is no less than 1 and no more than 140 characters long,
    and username must be between 1 and 14 characters long (inclusive) ).

    >>>is_mentioned( 'I LOVE UUUUU@MileyCrus' , 'MileyCyrus' )
    True
    >>>is_mentioned( ' KristenStewart is awesome!' , ' KristenStewart' )
    False
    """
    if  ('@' + username) in tweet :
        return True
    else:
        return False


def report_shortest(tweet1, tweet2):
    """  ( str ,  str)  -> bool
    
    Return the ' Tweet 1'  iff the first tweet is shorter than the second. 
    Return ' Tweet 2 ' iff the second tweet is shorter than the frist.
    Return ' Same length ' iff  tweet1 and tweet2 have the same length.
     tweet1 is the first tweet, tweet2 is the second tweet ( Both tweet1 and
     tweet2 are between 1 and 140 characters long(inclusive) ).

    >>>report_shortest( 'I love u', 'I love you more than anyone in my life')
    ' Tweet 1 '
    >>> report_shortest( 'Tax incidence is determined by which group (buyers
             or sellers) must write the check to the government.' ,  'Please
             check this out')
    ' Tweet 2 '
     >>>report_shortest( 'Boring People get Bored' , 'Bored People are Boring')
    ' Same length '
    """
    if  len(tweet1)  <  len(tweet2):
        return ' Tweet 1 '
    elif len(tweet1) > len(tweet2):
        return ' Tweet 2 '
    else:
        return ' Same length '



def is_reply(tweet):
    """  (str) -> bool
   Return True if the tweet is a reply. The tweet is a reply  when it starts
   with an @ symbol ( tweet is no less than 1 and no more than 140 characters
   long).

   >>>is_reply('@MileyCyrus I LOVE UUUUU' )
    True
    >>>is_reply( ' KristenStewart, you are awesome!')
    False
    """
    if  tweet[0] ==  '@':
        return True
    else:
        return False



def format_reply_to( username, tweet):
    """ (str, str) -> str

    Return a reply tweet which consists of a mention of that username
    followed by a space and the given tweet ( username represents a valid
    username or a valid username preceded by @, tweet represent a valid tweet
    that is no less than 1 and no more than 140 characters long).
    Return the number of extra characters followed by the string
    ' characters too long',  if the returned reply tweet contains more than 140
    characters.

    >>>format_reply_to('@MileyCyrus', 'YOU ARE AMAZING!')
    '@MileyCyrus YOU ARE AMAZING!'
    >>>format_reply_to( '@MilleyCyrus' , 'I can almost see it That dream I am
    dreaming But there is a voice inside my head saying You will never reach it
    Every step I am taking Every move I make feels Lost with no direction')
    '54 characters too long'
    """
    if  1<= len( username + tweet) <= 140:
        return username + ' ' + tweet
    elif len(username+tweet) > 140:
        return str(len(username+tweet)- 140)+' characters too long'


        
        









    
    
    

    

    
    


    

    
        
