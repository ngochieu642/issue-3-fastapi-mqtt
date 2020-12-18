.PHONY: local-fail
local-fail:
	docker-compose up --build -d api_fail

.PHONY: local-work
local-work:
	docker-compose up --build -d api_work