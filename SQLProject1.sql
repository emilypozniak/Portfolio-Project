Select Location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject..CovidDeaths 
order by 1,2

--Looking at the Total Cases vs. Total Deaths
--finding out the percentage of infected people who die in the United States

Select Location, date, total_cases, total_deaths, (total_deaths/total_cases) * 100 as DeathRate
From PortfolioProject..CovidDeaths 
where location like '%states%'
order by 1,2

--Looking at the Total Cases vs. Population
--determining what percentage of the population in the United States has ever contracted Covid

Select Location, date, population, total_cases, (total_cases/population) *100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths 
where location like '%states%'
order by 1,2

--Looking at countries with the highest infection rate compared to their population

Select Location, population, Max(total_cases) as HighestInfectionCount, Max((total_cases/population) *100) as PercentPopulationInfected
From PortfolioProject..CovidDeaths
Group by location, population 
order by PercentPopulationInfected desc

--Showing Countries with Highest Death Count per Population

Select Location, Max(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths
Group by location
order by TotalDeathCount desc

-- This shows the top ones as World, Europe, South America, Asia - We want to change that so it is by country

Select Location, Max(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths
Where Continent is not null
Group by location
order by TotalDeathCount desc

--The problem is fixed

--We now want to break it down by Continent
--The following shows the continents with the highest death count

Select location, Max(cast(Total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths
where continent is null
Group by location
order by TotalDeathCount desc

--Global Numbers

Select date, sum(new_cases) as total_cases, sum(cast(new_deaths as int)) as total_deaths, (sum(cast(new_deaths as int))/(sum(new_cases))) *100 as DeathPercentage
From PortfolioProject..CovidDeaths 
where continent is not null
Group by date
order by 1,2;

--Determining what percentage of the population has recieved at least one vaccine
--Using CTE

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
)
Select *, (RollingPeopleVaccinated/Population)*100 as PercentPopulationVaccinated
From PopvsVac;

--Create views to look at data in Tableau later

 Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date

Create View DeathRate as 
Select Location, date, total_cases, total_deaths, (total_deaths/total_cases) * 100 as DeathRate
From PortfolioProject..CovidDeaths 
where location like '%states%'


Create View PercentPopulationInfectedUS as
Select Location, date, population, total_cases, (total_cases/population) *100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths 
where location like '%states%'

