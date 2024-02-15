{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x16-api_advanced/tests":{"items":[{"name":"0-main.py","path":"0x16-api_advanced/tests/0-main.py","contentType":"file"},{"name":"1-main.py","path":"0x16-api_advanced/tests/1-main.py","contentType":"file"},{"name":"100-main.py","path":"0x16-api_advanced/tests/100-main.py","contentType":"file"},{"name":"2-main.py","path":"0x16-api_advanced/tests/2-main.py","contentType":"file"}],"totalCount":4},"0x16-api_advanced":{"items":[{"name":"tests","path":"0x16-api_advanced/tests","contentType":"directory"},{"name":"0-subs.py","path":"0x16-api_advanced/0-subs.py","contentType":"file"},{"name":"1-top_ten.py","path":"0x16-api_advanced/1-top_ten.py","contentType":"file"},{"name":"100-count.py","path":"0x16-api_advanced/100-count.py","contentType":"file"},{"name":"2-recurse.py","path":"0x16-api_advanced/2-recurse.py","contentType":"file"},{"name":"README.md","path":"0x16-api_advanced/README.md","contentType":"file"}],"totalCount":6},"":{"items":[{"name":"0x00-shell_basics","path":"0x00-shell_basics","contentType":"directory"},{"name":"0x01-shell_permissions","path":"0x01-shell_permissions","contentType":"directory"},{"name":"0x02-shell_redirections","path":"0x02-shell_redirections","contentType":"directory"},{"name":"0x03-shell_variables_expansions","path":"0x03-shell_variables_expansions","contentType":"directory"},{"name":"0x04-loops_conditions_and_parsing","path":"0x04-loops_conditions_and_parsing","contentType":"directory"},{"name":"0x05-processes_and_signals","path":"0x05-processes_and_signals","contentType":"directory"},{"name":"0x06-regular_expressions","path":"0x06-regular_expressions","contentType":"directory"},{"name":"0x07-networking_basics","path":"0x07-networking_basics","contentType":"directory"},{"name":"0x08-networking_basics_2","path":"0x08-networking_basics_2","contentType":"directory"},{"name":"0x09-web_infrastructure_design","path":"0x09-web_infrastructure_design","contentType":"directory"},{"name":"0x0A-configuration_management","path":"0x0A-configuration_management","contentType":"directory"},{"name":"0x0B-ssh","path":"0x0B-ssh","contentType":"directory"},{"name":"0x0C-web_server","path":"0x0C-web_server","contentType":"directory"},{"name":"0x0D-web_stack_debugging_0","path":"0x0D-web_stack_debugging_0","contentType":"directory"},{"name":"0x0E-web_stack_debugging_1","path":"0x0E-web_stack_debugging_1","contentType":"directory"},{"name":"0x0F-load_balancer","path":"0x0F-load_balancer","contentType":"directory"},{"name":"0x10-https_ssl","path":"0x10-https_ssl","contentType":"directory"},{"name":"0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter","path":"0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter","contentType":"directory"},{"name":"0x12-web_stack_debugging_2","path":"0x12-web_stack_debugging_2","contentType":"directory"},{"name":"0x13-firewall","path":"0x13-firewall","contentType":"directory"},{"name":"0x14-mysql","path":"0x14-mysql","contentType":"directory"},{"name":"0x15-api","path":"0x15-api","contentType":"directory"},{"name":"0x16-api_advanced","path":"0x16-api_advanced","contentType":"directory"},{"name":"0x17-web_stack_debugging_3","path":"0x17-web_stack_debugging_3","contentType":"directory"},{"name":"0x18-webstack_monitoring","path":"0x18-webstack_monitoring","contentType":"directory"},{"name":"0x1A-application_server","path":"0x1A-application_server","contentType":"directory"},{"name":"0x1B-web_stack_debugging_4","path":"0x1B-web_stack_debugging_4","contentType":"directory"},{"name":"command_line_for_the_win","path":"command_line_for_the_win","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":29}},"fileTreeProcessingTime":5.421498000000001,"foldersToFetch":[],"repo":{"id":531056351,"defaultBranch":"master","name":"alx-system_engineering-devops","ownerLogin":"Lordwill1","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-08-31T11:36:58.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/105258746?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1661946379.634948","canEdit":false,"refType":"branch","currentOid":"b7aabfb4db4157146b2e329278d9e2390865d57d"},"path":"0x16-api_advanced/tests/2-main.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","import sys","","if __name__ == '__main__':","    recurse = __import__('2-recurse').recurse","    if len(sys.argv) < 2:","        print(\"Please pass an argument for the subreddit to search.\")","    else:","        result = recurse(sys.argv[1])","    if result is not None:","        print(len(result))","    else:","        print(\"None\")"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":14,"end":24,"cssClass":"pl-en"},{"start":25,"end":36,"cssClass":"pl-s"},{"start":38,"end":45,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":68,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":24,"cssClass":"pl-en"},{"start":25,"end":28,"cssClass":"pl-s1"},{"start":29,"end":33,"cssClass":"pl-s1"},{"start":34,"end":35,"cssClass":"pl-c1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-c1"},{"start":21,"end":25,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":17,"cssClass":"pl-en"},{"start":18,"end":24,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":20,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Lordwill1/alx-system_engineering-devops/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Lordwill1/alx-system_engineering-devops/security/dependabot","repoSecurityAndAnalysisPath":"/Lordwill1/alx-system_engineering-devops/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"2-main.py","displayUrl":"https://github.com/Lordwill1/alx-system_engineering-devops/blob/master/0x16-api_advanced/tests/2-main.py?raw=true","headerInfo":{"blobSize":"334 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"f917cfa","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FLordwill1%2Falx-system_engineering-devops%2Fblob%2Fmaster%2F0x16-api_advanced%2Ftests%2F2-main.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"13","truncatedSloc":"12"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Lordwill1/alx-system_engineering-devops/discussions/new","newIssuePath":"/Lordwill1/alx-system_engineering-devops/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Lordwill1/alx-system_engineering-devops/blob/master/0x16-api_advanced/tests/2-main.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Lordwill1/alx-system_engineering-devops/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Lordwill1/alx-system_engineering-devops/raw/master/0x16-api_advanced/tests/2-main.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Lordwill1","repoName":"alx-system_engineering-devops","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Lordwill1/alx-system_engineering-devops/branches":{"post":"Xn_v_rVCF7A74PLFsrAXXmLn7ntVf2CK2HCLCBjRvZvLM7FAybZdagUouzO2Oh8Pzu-5k-kmO252Bb_Mn8Dleg"},"/repos/preferences":{"post":"ERtOxLVeFbRca7512z6CZigEoA7DJ2SXLlJCG1XVLeVzJarOFVwBujkQKfrRdbjCkumtHNG2r9dwfQWJGg5YeA"}}},"title":"alx-system_engineering-devops/0x16-api_advanced/tests/2-main.py at master · Lordwill1/alx-system_engineering-devops"}