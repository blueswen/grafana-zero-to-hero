import { css, cx } from '@emotion/css';
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { Organization } from 'types';
import { PanelProps, GrafanaTheme2 } from '@grafana/data';
import { Button, Combobox, useTheme2 } from '@grafana/ui';
import { getBackendSrv } from '@grafana/runtime';

interface Props extends PanelProps {}

const getStyles = (theme: GrafanaTheme2) => {
  return {
    container: css`
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    `,
    button: css`
      padding: 0 8px;
      position: relative;
    `,
    active: css`
      &::before {
        display: block;
        content: '';
        position: absolute;
        left: 0;
        right: 0;
        height: 2px;
        bottom: 0;
        border-radius: ${theme.shape.radius.default};
        background-image: ${theme.colors.gradients.brandHorizontal};
      }
    `,
  };
};

export const SimplePanel: React.FC<Props> = ({ options }) => {
  const [organizationsList, setOrganizationsList] = useState<Organization[]>([]);
  const [currentOrg, setCurrentOrg] = useState<number | null>(null);
  const theme = useTheme2();
  const styles = getStyles(theme);

  const baseURL = useMemo(() => {
    const url = window.location.href;
    if (url.includes('/d/')) {
      return url.split('/d/')[0];
    }
    return url.split('?')[0];
  }, []);

  const fetchOrganizations = useCallback(async () => {
    const result = await getBackendSrv().get('api/user/orgs');
    setOrganizationsList(
      result.map((item: any) => ({
        label: item.name,
        value: item.orgId,
      }))
    );
  }, []);

  const fetchCurrentOrg = useCallback(async () => {
    const user = await getBackendSrv().get('api/user');
    setCurrentOrg(user.orgId);
  }, []);

  useEffect(() => {
    fetchOrganizations();
    fetchCurrentOrg();
  }, [fetchOrganizations, fetchCurrentOrg]);

  switch (options.displayMode) {
    case 'select':
      return (
        <Combobox
          data-testid="org-select"
          options={organizationsList}
          value={currentOrg}
          onChange={(selected) => {
            if (selected?.value) {
              window.open(`${baseURL}/?orgId=${selected.value}`, '_self');
            }
          }}
        />
      );
    case 'button':
      return (
        <div className={cx(styles.container)}>
          {organizationsList.map((organization) => (
            <Button
              key={`org-${organization.value}`}
              data-testid={`org-${organization.value}`}
              variant="secondary"
              fill="solid"
              className={cx(styles.button, organization.value === currentOrg && styles.active, {
                active: organization.value === currentOrg,
              })}
              onClick={() => {
                window.open(`${baseURL}/?orgId=${organization.value}`, '_self');
              }}
            >
              {organization.label}
            </Button>
          ))}
        </div>
      );
    default:
      return <div className={cx(styles.container)}>Invalid display mode</div>;
  }
};
