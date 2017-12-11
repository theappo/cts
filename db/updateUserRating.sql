delimiter //
create trigger warnuser after insert on projectreviews for each row 
begin
  call updateUserRating(NEW.sender_id, NEW.receiver_id);
end; //  






create procedure updateUserRating(IN this_sender_id varchar(64), IN this_receiver_id varchar(64))
  begin
    declare ratings int(11);
    declare newrating decimal(4,3);
    declare numratings int(11);
    declare ratingsgiven int(11);
    declare numratingsgiven int(11);
    declare currentwarnings int(1);
    declare receiver_type int(1);
    declare sender_type int(1);

    select user_type into receiver_type from users where user_id = this_receiver_id;
    select user_type into sender_type from users where user_id = this_sender_id;
    select count(*) into numratings from projectreviews where receiver_id = this_receiver_id;
    select sum(rating) into ratings from projectreviews where receiver_id = this_receiver_id;
    
    if(receiver_type = 2) then
      update developers set avgrating = ratings / numratings where user_id = this_receiver_id;
      end if;
    if(receiver_type = 1) then
      update clients set avgrating = ratings / numratings where user_id = this_receiver_id;
      end if;
    if(ratings / numratings < 2 AND numratings > 5) then
      select warnings into currentwarnings from users where user_id = this_receiver_id;
      if(currentwarnings = 0) then
        update users set warnings = 1 where user_id = this_receiver_id;
        insert messages values ("SuperUser", this_receiver_id, "First Warning, rating too low", NOW());
        end if;
      if(currentwarnings = 1) then
        update users set warnings = 2 where user_id = this_receiver_id;
        insert messages values ("SuperUser", this_receiver_id, "Rating Too Low, Adding to Blacklist");
        end if;
      end if;
    select count(*) into numratingsgiven from projectreviews where sender_id = this_sender_id;
    select sum(rating) into ratingsgiven from projectreviews where sender_id = this_sender_id;
    if(ratingsgiven / numratingsgiven < 2 AND numratingsgiven > 8) then
      select warnings into currentwarnings from users where user_id = this_sender_id;
      if(currentwarnings = 0) then
        update users set warnings = 1 where user_id = this_sender_id;
        insert messages values ("SuperUser", this_sender_id, "First Warning: Avg rating sent < 2");
        end if;
      if(currentwarnings = 1) then
        update users set warnings = 2 where user_id = this_sender_id;
        insert messages values ("SuperUser", this_sender_id, "Second Warning: Avg rating sent < 2, adding to blacklist");
        end if;
      end if;
    if(ratingsgiven / numratingsgiven > 4 AND numratingsgiven > 8) then
      select warnings into currentwarnings from users where user_id = this_sender_id;
      if(currentwarnings = 0) then
        update users set warnings = 1 where user_id = this_sender_id;
        insert messages values ("SuperUser", this_sender_id, "First Warning: Avg rating sent > 4");
        end if;
      if(currentwarnings = 1) then
        update users set warnings = 2 where user_id = this_sender_id;
        insert messages values ("SuperUser", this_sender_id, "Second Warning: Avg rating sent > 4, adding to blacklist");
        end if;
      end if;
  end; //

        

    