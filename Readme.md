FS table:
	fs_user
		fsuid
		user_name
		email
		password
		location
		country
		registered_at
		updated_at
		
	fs_team
		fsteamid
		team_name
		added_at
		updated_at
	
	fs_team_members
		fstmid
		team_id
		member_id
		added_at
		
	fs_feature
		fsfeatureid
		title
		content
		created_by
		created_at
		updated_at
		
	fs_feature_holder (team who is holding the feature)
		fsfhid
		team_id
		feature_id
		added_at
		status
		
	fs_tact_coins
		fstcid
		team_id
		feature_id
		feature_coins
		status
		
	need to get:
		How much tact coins user-XYZ collected?
		How much tact coins team-ABC collected? - DONE
		How much do we owe to team-ABC which has to be released soon? - DONE
		Which team collected max coins in this week?
		
--------/
